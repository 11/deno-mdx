import sys
from json import dumps
from pprint import pformat
from pathlib import Path
from argparse import ArgumentParser

from .html import Html
from .markdown import Markdown
from .errors import MarkdownSyntaxError


def run(files=[], output='html', destination=None):
    for file in files:
        try:
            md = Markdown(file).markdown
            tokens = dumps(md, sort_keys=True, indent=2)
            if destination is None:
                if output.lower() == 'json':
                    print(tokens)
                elif output.lower() == 'html':
                    html = Html(md).html
                    print(html)
            else:
                if output.lower() == 'json':
                    destination.touch()
                    destination.write_text(tokens)
                elif output.lower() == 'html':
                    html = Html(md).html
                    destination.write_text(html)
        except MarkdownSyntaxError as err:
            print(err)


def parseargs():
    parser = ArgumentParser(prog='td', description='Parse markdown files')

    # positional args
    parser.add_argument('files', metavar='Files', type=Path, nargs='+', help='Set of files that will parsed')

    # optional args
    parser.add_argument('-d', '--destination', type=Path, default=None, help='Output directory')
    parser.add_argument('-o', '--output', type=str, choices=['json', 'html'], default='html', help='Specify output format (default: json)')

    return vars(parser.parse_args())


if __name__ == '__main__':
    kwargs = parseargs()
    run(**kwargs)
