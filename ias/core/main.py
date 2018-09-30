from parse import get_dataset_from_url
from models import Analysis, Data, Experiment, database
from collections import defaultdict
import datasets
import json
import filters


FILTERS = {
    'individual_filters': ['is_not_reverse', 'is_quantified', 'is_not_half_tryptic']
}

def create_tables():
    with database:
        database.create_tables([Data, Experiment, Analysis])

def new_analysis(analysis_name, datasets):
    URL_BASE = 'http://bfclabcomp4.scripps.edu/~vinograd/T_cells/{}/combined_dta.txt'

    datasets_for_analysis = []

    for d in datasets:
        name = '{}_{}um_{}_{}'.format(
            d.compound,
            str(d.concentration),
            d.proteome,
            'activated' if d.activation_state else 'naive'
        )
        datasets_for_analysis.append({
            'name': name,
            'datasets': [get_or_create_experiment(URL_BASE.format(l), name).id for l in d.links]
        })

    analysis = Analysis.create(name=analysis_name, datasets=json.dumps(datasets_for_analysis))
    return analysis

def apply_filters(analysis, filters_to_apply):
    if 'individual_filters' in filters_to_apply:
        apply_individual_filters(analysis, filters_to_apply['individual_filters'])

def apply_individual_filters(analysis, individual_filters):
    """Applies filters to individual rows of data, ie. before any aggregation."""
    # filters define which columns they each require
    # here we collect all of them so that we can include them in our select query
    required_columns = set(getattr(Data, filters.individual[f].requires) for f in individual_filters)
    required_columns.add(Data.id) # we always want id
    # keeps list of data items (rows) filtered out by individual filter
    filtered_out = defaultdict(list)

    for d in json.loads(analysis.datasets):
        query = Data.select(*required_columns).where(Data.experiment_id.in_(d['datasets']))
        for f in individual_filters:
            filtered_out[f].extend(apply_individual_filter(query, filters.individual[f]))
    return filtered_out

def apply_individual_filter(query, filter_obj):
    """Applies a given filter to all part of a query and returns data ids that do not pass."""
    return [x.id for x in query if not filter_obj.fn(getattr(x, filter_obj.requires))]

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
    analysis = new_analysis('katya_tcells', datasets.datasets)
    filtered = apply_filters(analysis, FILTERS)

if __name__ == '__main__':
    main()
