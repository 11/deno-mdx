import sys
import time
import logging
from argparse import ArgumentParser
from pathlib import Path

from errors import MarkdownSyntaxError
from markdown import Markdown as Md


logging.basicConfig(stream='sys.stdout', format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def _run(files=[], output_type='json', progress=False, destination=None, failfast=False, strict=False):
    for filename in files:
        try:
            file = Md(filename)
            result = file.parse(output=output_type)
            print(result)
        except MarkdownSyntaxError as md_err:
            logger.exception(md_error)
        except FileNotFoundError as fnf_err:
            logger.exception(f'`{filename}` does not exist')
        finally:
            if failfast:
                return


if __name__ == '__main__':
    parser = ArgumentParser(description='Parse markdown files', allow_abbrev=True)

    # positional args
    parser.add_argument('files', metavar='Files', type=Path, nargs='+', action='append', help='Set of files that will parsed')
    parser.add_argument('destination', metavar='Destination', type=Path, nargs='?', default=Path('./'), help='Output directory')

    # optional args
    parser.add_argument('--output', type=str, choices=['json', 'html'], default='json', help='Specify output format (default: json)')
    parser.add_argument('--progress', type=bool, default=False, help='Show time it took to parse each file (default: false)')
    parser.add_argument('--failfast', type=bool, default=False, help='Kill process if an error occurs (default: false)')
    parser.add_argument('--strict', type=bool, default=False, help='Kill process if invalid markdown syntax (default: false)')

    args = parser.parse_args()

    # _run(**args)

