from parse import get_dataset_from_url
from models import Analysis, Data, Experiment, database
from collections import defaultdict
import operator
import datasets
import itertools
import json
import filters


FILTERS = {
    'individual': ['is_not_reverse', 'is_quantified', 'is_not_half_tryptic'],
    'experiment': ['filter_20s']
}

def create_tables():
    with database:
        database.create_tables([Data, Experiment, Analysis])

def new_analysis(analysis_name, datasets):
    datasets_for_analysis = []

    for d in datasets['datasets']:
        # name = '{}_{}um_{}_{}'.format(
        #     d.compound,
        #     str(d.concentration),
        #     d.proteome,
        #     'activated' if d.activation_state else 'naive'
        # )
        name = d.proteome
        datasets_for_analysis.append({
            'name': name,
            'datasets': [get_or_create_experiment(datasets['base'].format(l), name).id for l in d.links]
        })

    analysis = Analysis.create(name=analysis_name, datasets=json.dumps(datasets_for_analysis))
    return analysis

def apply_filters(analysis, filters_to_apply):
    if 'individual' in filters_to_apply:
        exclude = apply_individual_filters(analysis, filters_to_apply['individual'])
        exclude = set().union(*exclude.values())
    if 'experiment' in filters_to_apply:
        return apply_experiment_filters(analysis, exclude, filters_to_apply['experiment'])


def apply_experiment_filters(analysis, exclude, experiment_filters):
    required_columns = get_required_columns(experiment_filters, 'experiment')
    seq_id_expression = Data.uniprot.concat(Data.clean_sequence).alias('seq_id')
    filtered_out = defaultdict(list)

    for dataset_group in json.loads(analysis.datasets):
        for d in dataset_group['datasets']:
            # experiment filters are applied on each experiment
            query = Data.select(*required_columns, seq_id_expression).where(Data.experiment_id == d & Data.id.not_in(exclude))
            raw = list(query.dicts())
            print(raw)
            raw = sorted(raw, key=operator.itemgetter('seq_id'))
            grouped = [list(g) for _, g in itertools.groupby(raw, key=operator.itemgetter('seq_id'))]

            for f in experiment_filters:
                filtered_out[f].extend(apply_experiment_filter(grouped, filters.experiment[f]))
    return filtered_out

def apply_experiment_filter(grouped_data, filter_obj):
    filtered_out = []
    for g in grouped_data:
        # filters return a list of booleans
        # True = keep, False = filter out
        filter_results = filter_obj.fn([x.get(filter_obj.requires) for x in g])
        ids_to_filter_out = [y[1]['id'] for y in zip(filter_results, g) if not y[0]]
        filtered_out.extend(ids_to_filter_out)
    return filtered_out

def apply_individual_filters(analysis, individual_filters):
    required_columns = get_required_columns(individual_filters, 'individual')
    # keeps list of data items (rows) filtered out by individual filter
    filtered_out = defaultdict(list)

    for d in json.loads(analysis.datasets):
        # individual filters are applied on replicate groups together
        query = Data.select(*required_columns).where(Data.experiment_id.in_(d['datasets']))
        for f in individual_filters:
            filtered_out[f].extend(apply_individual_filter(query, filters.individual[f]))
    return filtered_out

def apply_individual_filter(query, filter_obj):
    """Applies a given filter to all part of a query and returns data ids that do not pass."""
    return [x.id for x in query if not filter_obj.fn(getattr(x, filter_obj.requires))]

def get_required_columns(filters_to_apply, filter_type):
    """Applies filters to individual rows of data, ie. before any aggregation."""
    # filters define which columns they each require
    # here we collect all of them so that we can include them in our select query
    required_columns = set(getattr(Data, getattr(filters, filter_type)[f].requires) for f in filters_to_apply)
    required_columns.add(Data.id) # we always want id
    return required_columns


def get_or_create_experiment(url, name):
    experiment = get_experiment_from_url(url)
    return experiment if experiment else new_experiment(url, name)

def get_experiment_from_url(url):
    try:
        return Experiment.get(Experiment.source_url == url)
    except:
        return False

def new_experiment(url, name):
    raw = get_dataset_from_url(url)

    with database.atomic():
        experiment = Experiment.create(source_url=url, name=name)
        Data.bulk_create([Data(**r, experiment=experiment) for r in raw])
        return experiment

def main():
    create_tables()
    analysis = new_analysis('katya_gsdmp', datasets.gsdmd)
    filtered = apply_filters(analysis, FILTERS)
    return filtered

if __name__ == '__main__':
    main()
