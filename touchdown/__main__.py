import sys
import time
import logging
from argparse import ArgumentParser
from pathlib import Path

from .errors import MarkdownSyntaxError
from .markdown import Markdown as Md


logging.basicConfig(stream='sys.stdout')
logger = logging.getLogger(__name__)


def _run(files=[], output='json', verbose=False, destination=None, failfast=False, strict=False, pretty=False):
    total_time = 0

    for filename in files:
        try:
            file = Md(filename)
            result = None

            start = time.time()
            result = file.parse(output=output, pretty=pretty)
            end = time.time()

            elapsed_time = abs(start - end)
            total_time += elapsed_time

            if destination:
                # TODO: write output to file in cwd
                pass
            else:
                if verbose:
                    print(f'{filename}\n{result}')
                else:
                    print(result)
        except MarkdownSyntaxError as md_err:
            logger.exception(md_error)
            if strict:
                return
        except FileNotFoundError as fnf_err:
            logger.exception(f'`{filename}` does not exist')
        finally:
            if failfast:
                return

    if verbose:
        total_time_msg = f'Total time: {round(total_time, 6)} secs'
        line_break = f'\n{"-" * len(total_time_msg)}'
        print(line_break)
        print(total_time_msg)


if __name__ == '__main__':
    parser = ArgumentParser(prog='td', description='Parse markdown files')

    # positional args
    parser.add_argument('files', metavar='Files', type=Path, nargs='+', help='Set of files that will parsed')

    # optional args
    parser.add_argument('-d', '--destination', type=Path, default=None, help='Output directory')
    parser.add_argument('-o', '--output', type=str, choices=['json', 'html'], default='json', help='Specify output format (default: json)')
    parser.add_argument('-v', '--verbose', const=True, default=False, action='store_const', help='Log time it took to parse each file (default: false)')
    parser.add_argument('-f', '--failfast', const=True, default=False, action='store_const', help='Kill process if an error occurs (default: false)')
    parser.add_argument('-s', '--strict', const=True, default=False, action='store_const', help='Kill process if invalid markdown syntax (default: false)')
    parser.add_argument('-p', '--pretty', const=True, default=False, action='store_const', help='Format output')

    args = vars(parser.parse_args())
    _run(**args)

