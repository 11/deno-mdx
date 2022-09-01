import sys
import time
from json import dumps
from pathlib import Path
from pprint import pformat

import commandline
from html import Html
from markdown import Markdown
from errors import MarkdownSyntaxError

def _run(files=[], output='json', destination=None):
    total_time = 0

    for file in files:
        try:
            md = Markdown(file)
            tokens = md.tokenize()

            if destination is None:
                if output.lower() == 'json':
                    print(dumps(tokens, sort_keys=True, indent=2))
                elif output.lower() == 'html':
                    interpreter = Html(tokens)
                    html = interpreter.interpret()
                    print(html)
            else:
                with destination.open() as f:
                    if output.lower() == 'json':
                        f.write(dumps(tokens))
                    elif output.lower() == 'html':
                        interpreter = Html(tokens)
                        html = interpreter.interpret()
                        f.write(html)
        except MarkdownSyntaxError as md_err:
            print(md_err)

if __name__ == '__main__':
    kwargs = commandline.parseargs()
    _run(**kwargs)

