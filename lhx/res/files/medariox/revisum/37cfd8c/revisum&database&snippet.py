import os.path

from utils import get_project_root
from peewee import SqliteDatabase, Model, CharField, IntegerField


db = SqliteDatabase(None)


def maybe_init(repo_id, pr_number):
    path = get_project_root()
    db_dir = os.path.join(path, 'data', str(repo_id), 'snippets')
    if not os.path.isdir(db_dir):
        os.makedirs(db_dir)

    db_name = str(pr_number) + '.db'
    db_path = os.path.join(db_dir, db_name)
    db.init(db_path, pragmas={
        'journal_mode': 'wal',
        'cache_size': -1 * 64000,  # 64MB
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0})

    if not os.path.isfile(db_path):
        print('Snippet database created')
        create()


def create():
    db.create_tables([Snippet])


class Snippet(Model):

    snippet_id = CharField()
    start = IntegerField()
    source = CharField()
    target = CharField()
    source_lines = CharField()
    target_lines = CharField()

    class Meta:
        database = db
