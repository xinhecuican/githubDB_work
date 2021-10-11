from radon.raw import analyze


class Metrics(object):

    def __init__(self, code):
        self._code = code

        self.compute()

    def compute(self):
        print(self._code)
        result = analyze(self._code)
        print(result)
