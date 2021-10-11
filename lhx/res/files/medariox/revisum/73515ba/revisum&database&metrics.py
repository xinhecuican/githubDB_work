import os.path

from ..utils import get_project_root
from peewee import (
    BooleanField,
    SqliteDatabase,
    Model, CharField,
    FloatField,
    IntegerField
)


db = SqliteDatabase(None)


def maybe_init(repo_id):
    path = get_project_root()
    db_dir = os.path.join(path, 'data', str(repo_id))
    if not os.path.isdir(db_dir):
        os.makedirs(db_dir)

    db_name = 'metrics.db'
    db_path = os.path.join(db_dir, db_name)
    db.init(db_path, pragmas={
        'journal_mode': 'wal',
        'cache_size': -1 * 64000,  # 64MB
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0})

    if not os.path.isfile(db_path):
        create()
        print('Metrics database created for: {0}'.format(repo_id))


def create():
    db.create_tables([Metrics])


class Metrics(Model):

    name = CharField()
    low = IntegerField()
    med = IntegerField()
    high = IntegerField()
    very_high = IntegerField()

    class Meta:
        database = db
