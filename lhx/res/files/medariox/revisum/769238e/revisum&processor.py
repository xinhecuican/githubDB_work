import os
from pathlib import Path

from .pull_request import PullRequest
from .review import Review
from .snippet import Snippet
from .utils import get_project_root, gh_session
from .parsers.python_parser import PythonFileParser


class Processor(object):

    def __init__(self, repo):
        self._gh_session = gh_session()
        self._repo = self._gh_session.get_repo(repo)
        self.repo_name = self._repo.raw_data['full_name']
        self.repo_id = self._repo.raw_data['id']

    def first_run(self):
        cur_path = get_project_root()
        path = Path(os.path.join(cur_path, 'tmp'))

        snippets = []

        files = list(path.rglob('*.py'))
        for file_no, f in enumerate(files, 1):
            parser = PythonFileParser(0, self.repo_id, f)
            chunks = parser.parse(file_no=file_no)
            if not chunks:
                continue

            snippet_id = Snippet.make_id(0, file_no, 0, self.repo_id)
            snippet = Snippet(snippet_id, chunks, f, f)
            snippets.append(snippet)

        for snippet in snippets:
            snippet.save()
            for chunk in snippet._chunks:
                chunk.save(0, self.repo_id)

        return snippets

    def collect_snippets(self, update=True, limit=None):
        pulls = self._repo.get_pulls(state='all', sort='updated', direction='desc')
        newest_review = Review.newest_accepted(self._repo.id) if update else None
        limit = limit or 500

        review_count = 0
        snippets = []

        for pull in pulls:

            if newest_review and newest_review == pull.number:
                print('Reached newest review ({0})!'.format(newest_review))
                break

            pull_request = PullRequest(self._repo.id, pull.number, self._repo.full_name, pull.head.sha)
            if pull_request.is_valid:
                for snippet in pull_request.snippets:
                    print('-----------------------------------------------------------')
                    print(str(snippet))
                    print('-----------------------------------------------------------')

                snippets += pull_request.snippets
                pull_request.save()
                review_count += 1

                print('Total reviews: [{count}/{limit}]'.format(count=review_count, limit=limit))

            if review_count == limit:
                print('Reached reviews limit ({0})!'.format(limit))
                break

        return snippets
