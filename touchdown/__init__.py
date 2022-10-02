import json
from pathlib import Path

from .markdown import Markdown
from .errors import MarkdownSyntaxError
from .html import Html


def to_ast(file: Path):
    """ library function that will run markdown tokens formatted into a dictionary """
    return Markdown(file).markdown


def to_json(file: Path):
    """ library function that will run the entire conversion process to JSON output """
    md = Markdown(file).markdown
    output = Html(md).json
    return json.dumps(output)

def to_html(file: Path):
    """ library function that will run the entire conversion process """
    md = Markdown(file).markdown
    return Html(md).html


__all__ = [
    # general purpose functions that most users will interact with
    'to_ast',
    'to_html',
    'to_json',

    # actual parser, interpreter, and error classes - mainly for people
    # that want to customize how the HTML or Markdown is parsed
    'Markdown',
    'Html',
    'MarkdownSyntaxError',
]
