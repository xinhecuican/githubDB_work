from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token


class Snippet(object):

    def __init__(self, id, hunk, source, target):
        self.id = id
        self._hunk = hunk
        self.start = hunk.target_start
        self.end = 42
        self.source_file = source
        self.target_file = target

        self._target_lines = []
        self._source_lines = []
        self._target_tokens = []
        self._source_tokens = []

    def __str__(self):
        print('-------------------------------------------------------------')
        return '\n'.join(line for line in self.target_lines())

    def target_lines(self):
        if not self._target_lines:
            self._normalize_lines('target')
        return self._target_lines

    def source_lines(self):
        if not self._source_lines:
            self._normalize_lines('source')
        return self._source_lines
    
    @staticmethod
    def _verify_arg(arg):
        if arg not in ('target', 'source'):
            raise ValueError('{arg} value has to be either `target` or'
                             ' `source`.'.format(arg=arg))

    def _normalize_lines(self, origin='target'):
        self._verify_arg(origin)
        if origin == 'target':
            lines = self._hunk.target_lines()
            pre_char = '+'
            destination = self._target_lines
        elif origin == 'source':
            lines = self._hunk.source_lines()
            pre_char = '-'
            destination = self._source_lines

        for line in lines:
            single_line = str(line).rstrip()
            if single_line.startswith(pre_char):
                single_line = single_line.replace(pre_char, ' ', 1)
            destination.append(single_line)

    def as_tokens(self, origin='target'):
        self._verify_arg(origin)
        if origin == 'target':
            lines = self.target_lines()
        elif origin == 'source':
            lines = self.source_lines()

        lexed_lines = []
        for line in lines:
            tokens = lex(line, PythonLexer())
            tokens_list = []
            for token in tokens:
                if token[0] is Token.Text:
                    continue
                tokens_list.append(token[1])
            if tokens_list:
                lexed_lines.append(tokens_list)
        return lexed_lines
