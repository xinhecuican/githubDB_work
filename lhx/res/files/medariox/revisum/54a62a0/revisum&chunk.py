

class Chunk(object):

    def __init__(self, name, body, start, end):
        self.name = name
        self._body = body
        self.start = start
        self.end = end

        self._lines = []

        self.as_text()

    @property
    def lines(self):
        return self._lines

    def as_text(self):
        if not self._lines:
            for line_tokens in self._body:
                line = ''.join(line[1] for line in line_tokens)
                self._lines.append(line.rstrip())

        return self._lines
