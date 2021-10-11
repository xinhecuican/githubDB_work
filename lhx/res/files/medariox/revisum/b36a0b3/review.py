import re

import requests
from github import Github
from unidiff import PatchSet
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

from snippet import Snippet

g = Github("medariox", "comliebt92")

repo = g.get_repo("requests/requests")
pulls = repo.get_pulls(state='all')


class WeightedReview(object):

    def __init__(self, repo_id, pull):
        self._patch_content = None
        self.repo_id = repo_id
        self.id = pull.id
        self.title = pull.title
        self.state = pull.state
        self.merged = pull.merged
        self.patch_url = 'https://patch-diff.githubusercontent.com/raw/pymedusa/Medusa/pull/5643.patch'
        # self.patch_url = 'https://patch-diff.githubusercontent.com/raw/pymedusa/Medusa/pull/5813.patch'

        print(self.repo_id)

    @staticmethod
    def is_supported(target_file):
        if target_file.endswith('.py'):
            return True
        return False

    def added(self):
        matches = re.findall(r'^\+(?!\+|\s*\n)\s*(.*)', self.patch_content, re.M)
        lexed_matches = []
        for match in matches:
            tokens = lex(match, PythonLexer())
            tokens_list = []
            for token in tokens:
                if token[0] is Token.Text:
                    continue
                tokens_list.append(token[1])
            if tokens_list:
                lexed_matches.append(tokens_list)

        return lexed_matches

    def added_snippets(self):
        patch = PatchSet(self.patch_content)
        self.snippets = []
        for file_num, change in enumerate(patch, 1):
            print(change.target_file)
            if not self.is_supported(change.target_file):
                continue

            for i, hunk in enumerate(change, 1):
                snippet_id = str(file_num) + '-' + str(i) + '-' + str(self.id)
                snippet = Snippet(snippet_id, hunk, change.source_file, change.target_file)
                self.snippets.append(snippet)

        return self.snippets

    def removed(self):
        matches = re.findall(r'^\-(?!\-|\s*\n)\s*(.*)', self.patch_content, re.M)
        print(matches)
        for match in matches:
            bla = lex(match, PythonLexer())
            print(list(bla))

    @property
    def patch_content(self):
        """
        Gets the content of the pull request patch.

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
        Sets the content of the pull request patch.

        :param content: The content of the patch.
        :type: str
        """
        self._patch_content = content


for pull in pulls:
    reviews = pull.get_reviews()
    rev_len = reviews.totalCount
    if rev_len == 0:
        print("No reviews for {0}".format(pull.title))
        continue

    weighted_review = WeightedReview(repo.id, pull)
    break


added_snippets = weighted_review.added_snippets()

data = []
for snippet in added_snippets:
    data.append((snippet.id, snippet.as_tokens()))


def train_model(data, update=False):
    tagged_data = []
    for i, snippet in data:
        snippet_lines = []
        for line in snippet:
            snippet_lines += line
        print(snippet_lines)
        print(str(i))
        tagged_line = TaggedDocument(words=snippet_lines, tags=[i])
        tagged_data.append(tagged_line)

    if not update:
        model = Doc2Vec(vector_size=50,
                        alpha=0.025,
                        min_alpha=0.00025,
                        min_count=1,
                        dm=0)
        model.build_vocab(tagged_data)
    else:
        model = Doc2Vec.load("d2v.model")
        model.build_vocab(tagged_data, update=True)

    for epoch in range(100):
        print('iteration {0}'.format(epoch))
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.epochs)

    model.save("d2v.model")
    print("Model Saved")


def eval_model():
    model = Doc2Vec.load("d2v.model")

    tokens = "from six import text_type".split()
    new_vector = model.infer_vector(tokens)
    sims = model.docvecs.most_similar([new_vector])

    print(sims)
    print('--------------------------------------')
    print('For {input} matched {result}!'.format(input=tokens, result=sims[0][0]))


train_model(data)

for go in range(20):
    eval_model()
