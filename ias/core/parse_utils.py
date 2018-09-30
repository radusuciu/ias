from Bio import SeqIO
import hashlib
import inspect
import subprocess

def uniprot_db_from_fasta(path):
    db = list(SeqIO.parse(str(path), 'fasta'))
    uniprot_db = {}

    for item in db:
        try:
            if not 'Reverse_' in item.id:
                # Reversed entries can have the same id as the parent entry, and thus would
                # lead to overwriting the correct sequence for a given uniprot
                # with the reverse sequence
                _id = item.id.split('|')[1]
                uniprot_db[_id] = item
        except IndexError:
            pass

    return uniprot_db

def get_git_revision_hash():
    # credit to Yuji Tomita: https://stackoverflow.com/a/21901260/383744
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()


def hash_fn_source(fn):
    return hashlib.md5(inspect.getsource(fn).encode()).hexdigest()
