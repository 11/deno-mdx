from json import dumps
from pathlib import Path
from argparse import ArgumentParser

from .errors import MarkdownSyntaxError
from . import (
    to_ast, 
    to_html, 
    to_json,
)


def parseargs():
    parser = ArgumentParser(prog='touchdown', description='Parse markdown files')

    # positional args
    parser.add_argument('file', metavar='File', type=Path, help='files that will parsed')

    # optional args
    parser.add_argument('-O', '--output', type=str, choices=['JSON', 'HTML', 'AST'], default='HTML', help='Specify output format (default: HTML)')

    return vars(parser.parse_args())


def parse(file=None, output='HTML', destination=None):
    try:
        output = output.lower()
        if destination is None:
            if output == 'ast':
                print(to_ast(file))
            if output == 'html':
                print(to_html(file))
            if output == 'json':
                print(to_json(file))
    except MarkdownSyntaxError as err:
        print(err)


def touchdown():
    """ 
    this function is redundant, but necessary to make the touchdown a 
    useable from the commandline program 
    """

    kwargs = parseargs()
    parse(**kwargs)


if __name__ == '__main__':
    """ 
    this if statement is redundant, but necessary to make it so 
    you can run touchdown with `python -m touchdown <file>` 
    """

    touchdown()
