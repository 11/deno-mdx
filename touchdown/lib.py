from pathlib import Path


def lookahead(pattern, substr):
    """ lookahead determines if a pattern shows up in a string

    TODO: this function does not correctly handle all escape character scenarios.
          as an example, if we called `lookahead` with the following inputs:

            pattern = '*'
            substr = 'this is a test string \\*'

          the double backslash before the * is escaping the backslash
          character, NOT the * character. in the current implementation
          this would incorrectly assum the * character is being escaped.
          this edge case is pretty rare and can mostly be ignored - but
          should eventually be resolved later
    """
    next_idx = substr.find(pattern)
    if next_idx == -1:
        # return false if there is no closing pattern
        return False

    lag = substr[:next_idx]
    if len(lag) == 0:
        # if there are zero characters before the closing patter, this it's
        # not possible for the pattern to be escaped. therefore, it's always
        # a valid closing pattern
        return True
    elif len(lag) == 1 and substr[next_idx-1] == '\\':
        # if the closing pattern is escaped with a `\` character, then
        # that means the closing pattern should not be considered Mardown
        # syntax, but rather an actual character that belonds in the text.
        return False

    return True


def map_decorations_to_tokens(decorations):
    """ return correct token and tag values for text blocks wrapped in decorations """
    decors_token_map = {
        '*': 'bold',
        '_': 'underline',
        '~': 'strikethrough',
        '/': 'italic',
        '`': 'code',
    }

    decors_tag_map = {
        '*': 'b',
        '_': 'u',
        '~': 'strikethrough',
        '/': 'i',
        '`': 'code',
    }

    return {
        'token': [decors_token_map[decor] for decor in decorations],
        'tag': [decors_tag_map[decor] for decor in decorations]
    }


def readfile(file: Path, filetype: str=None):
    """ performs error handling on files before creating a file iteartor """

    if not file.exists:
        raise FileNotFoundError(f'{filename} does not exist') from None
    elif filetype and file.suffix != filetype:
        raise ValueError(f'{filename} is not of type {file_type}') from None

    def _readfile():
        with file.open() as f:
            for line in f:
                yield line

    return _FileIterator(_readfile)


class _FileIterator:
    """ L1 Parser file iterator

    This FileIterator class allows the parsing loop to remember 1 line previous. If the parsing loop
    wants to go back an iteration, the parsing loop can call `backstep()` to undo the last
    iteration. This is useful for parsing multiline blocks - such as lists and codeblocks that
    could potentially be several lines long.
    """

    def __init__(self, reader):
        self._prev = None
        self._backstep = None

        self._reader = reader()

    def __iter__(self):
        return self

    def __next__(self):
        if self._backstep:
            line = self._backstep
            self._backstep = None
            return line

        line = next(self._reader, None)
        if not line:
            raise StopIteration

        self._prev = line
        return line

    def backstep(self):
        self._backstep = self._prev
