import requests

from database import maybe_init
from snippet import Snippet
from unidiff import PatchSet
from review import ValidReview


class ReviewedPullRequest(object):

    def __init__(self, repo_id, pull):
        self._patch_content = None
        self._valid_reviews = []
        self._pull = pull
        self.repo_id = repo_id
        self.number = pull.number
        self.title = pull.title
        self.state = pull.state
        self.merged = pull.merged
        self.patch_url = pull.patch_url
        # self.patch_url = 'https://patch-diff.githubusercontent.com/raw/pymedusa/Medusa/pull/5643.patch'
        # self.patch_url = 'https://patch-diff.githubusercontent.com/raw/pymedusa/Medusa/pull/5813.patch'

    @staticmethod
    def is_supported(target_file):
        if target_file.endswith('.py'):
            return True
        return False

    def snippets(self):
        patch = PatchSet(self.patch_content)

        self.snippets = []
        for file_no, change in enumerate(patch, 1):
            if not self.is_supported(change.target_file):
                continue

            for hunk_no, hunk in enumerate(change, 1):
                snippet_id = '-'.join([str(hunk_no), str(file_no), str(self.number), str(self.repo_id)])
                snippet = Snippet(snippet_id, hunk, change.source_file, change.target_file)
                self.snippets.append(snippet)

        return self.snippets

    @property
    def patch_content(self):
        """
        Get the content of the pull request patch.

        :return: The content of the patch.
        :type: str
        """
        if not self._patch_content:
            response = requests.get(self.patch_url)
            self._patch_content = response.text

        return self._patch_content

    @patch_content.setter
    def patch_content(self, content):
        """
        Set the content of the pull request patch.

        :param content: The content of the patch.
        :type: str
        """
        self._patch_content = content

    @property
    def valid_reviews(self):
        if self._valid_reviews or self.has_valid_review():
            return self._valid_reviews

    def has_valid_review(self):
        reviews = self._pull.get_reviews()
        rev_len = reviews.totalCount
        if rev_len == 0:
            print('No review for: {0}'.format(self.title))
            return False

        for review in reviews:
            if review.body != '':
                self._valid_reviews.append(ValidReview(
                    self.repo_id, self.number, review))

        if self._valid_reviews:
            print('Found reviews for: {0}'.format(self.title))
            return True

        print('No valid review for: {0}'.format(self.title))
        return False

    def save(self):
        if self.valid_reviews:
            maybe_init(self.repo_id)
            for valid_review in self._valid_reviews:
                valid_review.save()
