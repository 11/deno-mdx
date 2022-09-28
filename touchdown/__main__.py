from json import dumps
from pathlib import Path
from argparse import ArgumentParser

from .html import Html
from .markdown import Markdown
from .errors import MarkdownSyntaxError


def parseargs():
    parser = ArgumentParser(prog='touchdown', description='Parse markdown files')

    # positional args
    parser.add_argument('files', metavar='Files', type=Path, nargs='+', help='Set of files that will parsed')

    # optional args
    parser.add_argument('-D', '--destination', type=Path, default=None, help='Output directory')
    parser.add_argument('-O', '--output', type=str, choices=['JSON', 'HTML', 'AST'], default='HTML', help='Specify output format (default: HTML)')

    return vars(parser.parse_args())


def parse(files=[], output='HTML', destination=None):
    for file in files:
        try:
            md_tokens = Markdown(file).markdown
            output = output.lower()

            if destination is None:
                if output == 'ast':
                    ast = dumps(md_tokens, sort_keys=True, indent=2)
                    print(tokens)
                if output == 'html':
                    html = Html(md_tokens).html
                    print(html)
                if output == 'json':
                    pass

            if destination:
                if output == 'ast':
                    destination.touch()
                    destination.write_text(tokens)
                if output == 'html':
                    html = Html(md_tokens).html
                    destination.write_text(html)
                if output == 'json':
                    pass

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
