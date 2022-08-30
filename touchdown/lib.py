from pathlib import Path


MARKDOWN_TOKENS = {
    # https://www.debuggex.com/r/yJLwFDiFjDuifTSr
    'header': r'^(#{1,6}?) (.*?)$',

    # https://www.debuggex.com/r/4xeF1p18gQjjhAe9
    'blockquote': r'^\> [\s\S]*$',

    # https://www.debuggex.com/r/s2BZUI9PedP0m5O-
    'ordered_list': r'^\s*[0-9]{1,}. ([\s\S]*)\n$',

    # https://www.debuggex.com/r/9hQERKefFNj_3CsR
    'unordered_list': r'^\s*- ([\s\S]*)\n$',

    # https://www.debuggex.com/r/u64sYbgHehYd5zet
    'image': r'^!\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/dnmmbV9HXMOBFQPa
    'link': r'^\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/7D4R7b9LVt8QbJ1l
    'codeblock': r'^```$',
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

    This FileReader class allows the parsing loop to remember 1 line previous. If the parsing loop
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
