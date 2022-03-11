from pathlib import Path


def read_file(filename, file_type:str=None):
    if not filename:
        raise ValueError(f'Must enter filename')

    file = Path(filename)
    if not file.exists:
        raise FileNotFoundError(f'{filename} does not exist')
    if file_type and file.suffix != file_type:
        raise ValueError(f'{filename} is not of type {file_type}')

    with file.open() as f:
        for line in f:
            yield line


def write_file(data: dict, output_file: str):
    """ pprints to file """
    if not data:
        raise ValueError(f'Must enter filename')
    elif not output_file:
        raise ValueError(f'Must enter filename')


    output = Path(output_file)
    if not file.exists:
        pass


def write_json_stdout(data: dict):
    """ pprints to stdout """
    pass


def write_(data: dict):
    pass
