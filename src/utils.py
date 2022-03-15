from pathlib import Path


def read_file(file: Path, filetype:str=None):
    """ performs error handling on files before creating a file iteartor """

    if not file.exists:
        raise FileNotFoundError(f'{filename} does not exist')
    elif filetype and file.suffix != filetype:
        raise ValueError(f'{filename} is not of type {file_type}')

    def _readfile():
        with file.open() as f:
            for line in f:
                yield line

    return FileReader(_readfile)


class FileReader:
    """ L1 Parser file iterator

    This FileReader class allows the parsing loop to look 1 line ahead. If the parsing loop
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
