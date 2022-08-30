from pathlib import Path
from argparse import ArgumentParser


def parseargs():
    parser = ArgumentParser(prog='td', description='Parse markdown files')

    # positional args
    parser.add_argument('files', metavar='Files', type=Path, nargs='+', help='Set of files that will parsed')

    # optional args
    parser.add_argument('-d', '--destination', type=Path, default=None, help='Output directory')
    parser.add_argument('-o', '--output', type=str, choices=['json', 'html'], default='json', help='Specify output format (default: json)')

    args = vars(parser.parse_args())
    return args

