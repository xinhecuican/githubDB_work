import os.path

from ..snippet import Snippet
from ..utils import get_project_root

from peewee import (
    BooleanField,
    SqliteDatabase,
    BlobField,
    Model, CharField,
    FloatField,
    IntegerField
)


db = SqliteDatabase(None)


def maybe_init(repo_id, snippet_id):
    path = get_project_root()
    db_dir = os.path.join(path, 'data', str(repo_id), 'chunks')
    if not os.path.isdir(db_dir):
        os.makedirs(db_dir)

    pr_number = Snippet.pr_number(snippet_id)

    name = '{0}-{1}'.format(pr_number, repo_id)
    db_name = name + '.db'
    db_path = os.path.join(db_dir, db_name)
    db.init(db_path, pragmas={
        'journal_mode': 'wal',
        'cache_size': -1 * 64000,  # 64MB
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0})

    if not os.path.isfile(db_path):
        create()
        print('Chunks database created for: {0}'.format(name))


def create():
    db.create_tables([Chunk])


class Chunk(Model):

    chunk_id = CharField()
    name = CharField()
    no = IntegerField()
    file_no = IntegerField()
    start = IntegerField()
    end = IntegerField()
    body = BlobField()

    class Meta:
        database = db
