from pathlib import Path

from .markdown import Markdown
from .html import Html


def markdown(file: Path):
    return Markdown(file).markdown


def html(file: Path):
    """ library function that will run the entire conversion process """
    md = Markdown(file).markdown
    return Html(md).html


__all__ = ['markdown', 'html']
