
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


class SnippetsTrainer(object):

    def __init__(self, snippets):
        self._snippets = snippets

    @property
    def snippets(self):
        """
        Gets all the snippets used for the training.

        :return: All the availible snippets.
        :type: list
        """
        if not isinstance(self._snippets, list):
            self._snippets = list(self._snippets)

        return self._snippets

    def train(self, update=False):
        tagged_data = []
        for snippet in self.snippets:
            snippet_lines = []
            for line in snippet.as_tokens():
                snippet_lines += line
            print(snippet_lines)
            tagged_line = TaggedDocument(words=snippet_lines, tags=[snippet.id])
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
