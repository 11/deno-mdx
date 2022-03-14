def read_file(file: Path, filetype:str=None):
    if not file.exists:
        raise FileNotFoundError(f'{filename} does not exist')
    elif filetype and file.suffix != filetype:
        raise ValueError(f'{filename} is not of type {file_type}')

    def _fileiter():
        with file.open() as f:
            for line in f:
                yield line

    return Reader(_fileiter)


class Reader:
    """ L1 Parser iterator helper """

    def __init__(self, fileiter):
        self._prev_line = None
        self._backstep = None
        self._fileiter = fileiter

    def __next__(self):
        if self._backstep:
            line = self._backstep
            self._backstep = None
            return line

        line = next(self._fileiter())
        self.prev = line

        return line

    def backstep(self, line):
        self._backstep = self._prev
