"""Le models."""
from parse_utils import get_git_revision_hash
from peewee import *
import datetime

database = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = database

class Analysis(BaseModel):
    """Data on analyses of multiple datasets."""
    name = TextField()
    analysis_hash = TextField(default=get_git_revision_hash)
    date = DateField(default=datetime.datetime.now)
    datasets = TextField()
    filters = TextField(null=True)

class Experiment(BaseModel):
    """Holds experimental metadata."""
    name = TextField()
    source_url = TextField(unique=True)
    date = DateField(default=datetime.datetime.now)
    meta = TextField(null=True)

class Data(BaseModel):
    """Holds actual experimental data."""
    experiment = ForeignKeyField(Experiment)
    uniprot = TextField(index=True)
    description = TextField()
    symbol = TextField(index=True)
    sequence = TextField(index=True)
    cimage_sequence = TextField(index=True)
    clean_sequence =TextField(index=True)
    residue = IntegerField(index=True)
    mass = FloatField()
    ratio = FloatField(index=True)
    stats = TextField()
    run = IntegerField()
    charge = IntegerField()
    segment = IntegerField()
    link = TextField()
    meta = TextField(null=True)
