from parse_utils import uniprot_db_from_fasta
import requests

delchars = {ord(c): None for c in map(chr, range(256)) if not c.isalpha()}
delchars_except_mod = {ord(c): None for c in map(chr, range(256)) if not c.isalpha() and not c == '*'}
uniprot_db = uniprot_db_from_fasta('db.txt')

entry_headers = [
    'uniprot',
    'description',
    'symbol',
    'sequence',
    'mass',
    'ratio',
    'stats',
    'run',
    'charge',
    'segment',
    'link',
]

headers = [
    'cimage_sequence',
    'residue',
    'clean_sequence'
] + entry_headers

headers_to_cast = {
    'mass': float,
    'ratio': float,
    'run': int,
    'charge': int ,
    'segment': int
}


def get_dataset_from_url(url: str):
    """Get raw dataset from  given url."""
    res: Response = requests.get(url)
    # raise exception if the url is not found
    res.raise_for_status()

    raw_dataset: str = res.text
    return parse(raw_dataset)


def parse(raw_dataset: str):
    data = []
    cimage_sequence = ''

    for line in raw_dataset.splitlines()[1:]:
        split_line = [i.strip() for i in line.split('\t') if i.strip()]

        if split_line[0].isdigit():
            # group header
            entry = dict.fromkeys(headers)
            cimage_sequence = split_line[1]
        else:
            # individual peptides
            entry = dict(zip(entry_headers, split_line))

            entry['cimage_sequence'] = cimage_sequence
            entry['clean_sequence'] = entry['sequence'].split('.')[1].translate(delchars)
            entry['residue'] = annotate_residue(entry['uniprot'], entry['sequence'])

            for h, t in headers_to_cast.items():
                entry[h] = t(entry[h])

            data.append(entry)

    return data


def annotate_residue(uniprot, sequence):
    if uniprot.startswith('Reverse_'):
        return 0

    protein_sequence = uniprot_db[uniprot].seq

    # take sequence between tryptic terminii and remove all modifications
    # except *, which indicates that the residue is labeled
    sequence = sequence.split('.')[1].translate(delchars_except_mod)
    position_in_sequence = sequence.index('*')
    sequence = sequence.replace('*', '')
    sequence_position_in_protein = protein_sequence.find(sequence)
    residue = sequence_position_in_protein + position_in_sequence

    return residue


