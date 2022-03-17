from argparse import ArgumentParser

from errors import MarkdownSyntaxError
from markdown import Markdown as Md


def _parse(files=[], output_type='json'):
    output_type = output_type.lower()
    if output_type != 'json' or output_type != 'html':
        # TODO: raise some error
        return

    for filename in files:
        file = Md(filename)
        try:
            result = file.parse(output=output_type)
            print(result)
        except MarkdownSyntaxError as md_err:
            print(md_err)
            return


parser = ArgumentParser(description='', allow_abbrev=True)
parser.add_argument(
    '--format',
    dest='',
    type=str,
    help='',
)

args = parser.parse_args()

