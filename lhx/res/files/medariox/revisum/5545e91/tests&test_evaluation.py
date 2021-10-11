import os
import sys
sys.path.append('../revisum')

from pathlib import Path

import pytest
from revisum.snippet import Snippet
from gensim.models.doc2vec import Doc2Vec


tests_data = os.path.join(Path(__file__).parent, 'data')


code_to_find = [
    """
    def test_preparing_url(self, url, expected):

    def normalize_percent_encode(x):
        # Helper function that normalizes equivalent
        # percent-encoded bytes before comparisons
        for c in re.findall(r'%[a-fA-F0-9]{2}', x):
            x = x.replace(c, c.upper())
        return x

    r = requests.Request('GET', url=url)
    p = r.prepare()
    assert normalize_percent_encode(p.url) == expected
    """
]


def evaluate():

    tokens = Snippet.tokenize(code_to_find)
    print(tokens)

    for test_dir in os.listdir(tests_data):

        repo_id, iterations, snippets = test_dir.split('_')

        model_path = os.path.join(tests_data, test_dir, 'd2v.model')
        model = Doc2Vec.load(model_path)

        new_vector = model.infer_vector(tokens)
        sims = model.docvecs.most_similar([new_vector])
        confidence = sims[0][1]
        print(sims)

        print('--------------------------------------')
        print('For {input} matched {result}!'.format(
            input=tokens, result=sims[0][0]))

        matched_code = Snippet.load(sims[0][0], path=os.path.join(tests_data, test_dir))
        print(matched_code)
        matched_tokens = Snippet.tokenize(str(matched_code))
        print(matched_tokens)

        # assert confidence > 0.95

        snippet_id = sims[0][0]
        print(snippet_id)

        # assert snippet_id == '2-1-4915-1362490'


evaluate()
