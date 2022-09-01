import re
import pdb
from pathlib import Path
from io import StringIO as StringBuilder

from errors import MarkdownSyntaxError
from constants import SPECIAL_CHARS, MARKDOWN_REGEXS
from lib import (
    readfile,
    lookahead,
    map_decorations_to_tokens,
)


class Markdown:
    """ Markdown Tokenizer

    The Markdown class's only responsibility is to tokenize the code within a markdown
    file. Tokenize in this context means to catagorize each block of markdown code, and
    store the relevant information into a dictionary. After reading an entire file, this
    class will output a dictionary that contains meta data about the file that was just
    parsed, and the tokenized markdown code.
    """

    def __init__(self, file):
        self._filepath = Path(file)
        self._lineno = 0
        self._reader = None

    def __repr__(self):
        return f'File {self._filepath.name} - Lines processed {self._lineno}'

    def __iter__(self):
        self._reader = readfile(self._filepath)
        return self

    def __next__(self):
        line = next(self._reader, None)
        if not line:
            raise StopIteration

        self._lineno += 1

        if re.match(MARKDOWN_REGEXS['header'], line):
            return self._parse_header(line)
        elif re.match(MARKDOWN_REGEXS['blockquote'], line):
            return self._parse_blockquote(line)
        elif re.match(MARKDOWN_REGEXS['ordered_list'], line):
            return self._parse_ordered_list(self._reader)
        elif re.match(MARKDOWN_REGEXS['unordered_list'], line):
            return self._parse_unordered_list(self._reader)
        elif re.match(MARKDOWN_REGEXS['image'], line):
            return self._parse_image(line)
        elif re.match(MARKDOWN_REGEXS['codeblock'], line):
            return self._parse_codeblock(line)
        else:
            return self._parse_paragraph(line)

    @property
    def filename(self):
        return self._filepath.name

    def tokenize(self):
        return {
            'filename': self._filepath.name,
            'content': [token for token in self],
        }

    def _parse_header(self, line):
        match = re.findall(MARKDOWN_REGEXS['header'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        header, content = match[0]
        return {
            'type': 'header',
            'tag': f'h{len(header)}',
            'content': self._parse_text(content),
        }

    def _parse_blockquote(self, line):
        match = re.findall(MARKDOWN_REGEXS['blockquote'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        blockquote, content = match[0]
        return {
            'type': 'blockquote',
            'tag': 'blockquote',
            'content': self._parse_text(content),
        }

    def _parse_codeblock(self, line, reader):
        match = re.findall(MARKDOWN_REGEXS['codeblock'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        codeblock, content = match[0]
        return {
            'type': 'codeblock',
            'tag': 'code-block',
            'content': content,
            'language': None,
        }

    def _parse_list(self, reader, list_type, list_tag):
        reader.backstep() # reset the file generator back to the beginning of the ordered list

        output = {
            'type': list_type,
            'tag': list_tag,
            'content': [],
        }

        while (line := next(reader, None)):
            match = None
            if re.match(MARKDOWN_REGEXS['ordered_list'], line):
                match = re.findall(MARKDOWN_REGEXS['ordered_list'], line)
            elif re.match(MARKDOWN_REGEXS['unordered_list'], line):
                match = re.findall(MARKDOWN_REGEXS['unordered_list'], line)
            else:
                reader.backstep()
                break

            if len(match) != 1:
                raise MarkdownSyntaxError(self._file, self._lineno, '')

            content = match[0]
            output['content'].append({
                'type': 'listitem',
                'tag': 'li',
                'content': self._parse_text(content),
            })

        return output

    def _parse_ordered_list(self, reader):
        return self._parse_list(reader, 'ordered_list', 'ol')

    def _parse_unordered_list(self, reader):
        return self._parse_list(reader, 'unordered_list', 'ul')

    def _parse_image(self, line):
        match = re.findall(MARKDOWN_REGEXS['image'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        uri, alt_text = match[0]
        return {
            'type': 'image',
            'tag': 'img',
            'url': uri,
            'alt': alt_text,
        }

    def _parse_link(self, line):
        pass

    def _parse_decoration(self, line, seek=0):
        decorations = []

        active = set()
        builder = StringBuilder()
        idx = seek
        while True:
            lag = line[idx-1] if idx > 0 else ''
            char = line[idx]

            if lag != '\\' and char in SPECIAL_CHARS:
                block = { 'type': 'text', 'content': builder.getvalue() }
                block.update(map_decorations_to_tokens(active))
                decorations.append(block)
                builder.close()
                builder = StringBuilder()

                if char not in active:
                    active.add(char)
                else:
                    active.remove(char)
            else:
                builder.write(char)

            idx += 1
            prev = line[idx-1]
            char = line[idx]

            if not (idx < len(line) and len(active) > 0):
                break

        if len(active) > 0:
            # if the entire line of text was parsed and there are missing
            # closing decoration characters, raise a syntax error
            active_decorations = list(active)
            raise MarkdownSyntaxError(self._file, self._lineno, f'{active_decorations[0]} needs a matching closing character')

        return decorations, idx

    def _parse_text(self, line):
        content = []
        builder = StringBuilder()

        idx = 0
        while idx < len(line):
            lag = line[idx-1] if idx > 0 else ''
            char = line[idx]

            if idx == len(line) - 1:
                # if the loop is on its last iteration, append the last text
                # node to the output, and close the string builder buffer
                builder.write(char)
                content.append({
                    'type': None,
                    'tag': None,
                    'content': builder.getvalue()
                })
                builder.close()
            elif char in SPECIAL_CHARS and lag != '\\' and lookahead(char, line[idx+1:]) == False:
                # if a special character is found but there is no closing special
                # character, stop parsing and print a MarkdownSyntaxError
                raise MarkdownSyntaxError(self._file, self._lineno, f'{char} needs a matching closing character')
            elif char in SPECIAL_CHARS and lag != '\\' and lookahead(char, line[idx+1:]):
                # if reading a special character that isn't escaped and
                # the rest of the string contains a closing character, end
                # the current text node and start parsing deocrations
                content.append({
                    'type': None,
                    'tag': None,
                    'content': builder.getvalue()
                })
                builder.close()
                builder = StringBuilder()

                # `decorations` is a list of decoration text nodes to append to the output
                # `seek` is the index that `idx` should jump forward to
                decorations, seek = self._parse_decoration(line, seek=idx)
                content += decorations
                idx = seek
            else:
                builder.write(char)

            idx += 1

        return {
            'type': 'text',
            'content': content,
        }

    def _parse_paragraph(self, line):
        return {
            'type': 'paragraph',
            'tag': 'p',
            'content': [self._parse_text(line)],
        }
