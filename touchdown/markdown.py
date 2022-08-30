import re
from pathlib import Path
from io import StringIO as StringBuilder

from lib import readfile
from lib import MARKDOWN_TOKENS as tks
from errors import (
    MarkdownSyntaxError,
    OutputTypeError,
)


def map_decorations_to_tokens(decorations):
    """ take tokens inside """
    decors_token_map = {
        '*': 'bold',
        '_': 'underline',
        '~': 'strikethrough',
        '/': 'italic',
        '`': 'code',
    }

    decors_tag_map = {
        '*': 'b',
        '_': 'u',
        '~': 'strikethrough',
        '/': 'i',
        '`': 'code',
    }

    return {
        'token': [decors_token_map[decor] for decor in decorations],
        'tag': [decors_tag_map[decor] for decor in decorations]
    }


class Markdown:
    def __init__(self, file):
        self._filepath = Path(file)
        self._lineno = 0

        self._reader = None

    def __repr__(self):
        return f'File {self._filepath.name} - Lines processed {self._lineno}'

    def __str__(self):
        if self._output == 'html':
            # TODO: pprint HTML
            pass

        return pformat(self.parse())

    def __iter__(self):
        self._reader = readfile(self._filepath)
        return self

    def __next__(self):
        line = next(self._reader, None)
        if not line:
            raise StopIteration

        self._lineno += 1

        if re.match(tks['header'], line):
            return self._parse_header(line)
        elif re.match(tks['blockquote'], line):
            return self._parse_blockquote(line)
        elif re.match(tks['ordered_list'], line):
            return self._parse_ordered_list(self._reader)
        elif re.match(tks['unordered_list'], line):
            return self._parse_unordered_list(self._reader)
        elif re.match(tks['image'], line):
            return self._parse_image(line)
        elif re.match(tks['codeblock'], line):
            return self._parse_codeblock(line)
        elif re.match(tks['link'], line):
            return self._parse_image(line)
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
        match = re.findall(tks['header'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        header, content = match[0]
        return {
            'type': 'header',
            'tag': f'h{len(header)}',
            'content': self._parse_text(content),
        }

    def _parse_blockquote(self, line):
        match = re.findall(tks['blockquote'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        blockquote, content = match[0]
        return {
            'type': 'blockquote',
            'tag': 'blockquote',
            'content': self._parse_text(content),
        }

    def _parse_codeblock(self, line, reader):
        match = re.findall(tks['codeblock'], line)
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
            if re.match(tks['ordered_list'], line):
                match = re.findall(tks['ordered_list'], line)
            else:
                reader.backstep()
                break

            if len(match) != 1:
                raise MarkdownSyntaxError(self._file, self._lineno, '')

            _, content = match[0]
            output['content'].append({
                'type': 'listitem',
                'tag': 'li',
                'content': self._parse_text(content),
            })

        return output

    def _parse_ordered_list(self, reader):
        return self._parse_list(reader, 'ordered_list', 'ol')

    def _parse_unordered_list(self, line):
        return self._parse_list(reader, 'unordered_list', 'ul')

    def _parse_image(self, line):
        match = re.findall(tks['image'], line)
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

    # TODO: CLEAN UP
    def _parse_decoration(self, line, seek=0):
        decors = set(['*', '_', '~', '/', '`'])
        pool = set()
        output = []

        text = None
        prev = None
        idx = seek
        char = line[idx]
        while idx < len(line):
            if prev == '\\' and char in decors:
                idx += 1
                prev = line[idx-1]
                char = line[idx]
                continue
            elif prev != '\\' and char in decors:
                if len(pool) == 0:
                    pool.add(char)
                    block = { 'type': 'text', 'content': None }
                    block.update(map_decorations_to_tokens(pool))
                    output.append(block)
                    text = StringBuilder()
                elif char not in pool:
                    # close off old decoration string
                    output[-1]['content'] = text.getvalue()
                    text.close()
                    text = StringBuilder()

                    # append new decoration stirng
                    pool.add(char)

                    block = { 'type': 'text', 'content': None }
                    block.update(map_decorations_to_tokens(pool))
                    output.append(block)
                elif char in pool and len(pool) > 1:
                    output[-1]['content'] = text.getvalue()
                    text.close()
                    text = StringBuilder()
                    pool.remove(char)

                    block = { 'type': 'text', 'content': None }
                    block.update(map_decorations_to_tokens(pool))
                    output.append(block)
                elif char in pool and len(pool) == 1:
                    output[-1]['content'] = text.getvalue()
                    text.close()
                    pool.remove(char)
                    return output, idx+1

                idx += 1
                prev = line[idx-1]
                char = line[idx]
                continue

            text.write(char)

            idx += 1
            prev = line[idx-1]
            char = line[idx]


        if len(pool) > 0:
            output[-1]['content'] = text.getvalue()
            text.close()

        return output, None

    def _parse_text(self, line):
        decors = set(['*', '_', '~', '/', '`'])
        output = {
            'type': 'text',
            'content': [],
        }

        idx = 0
        text = StringBuilder()
        while idx < len(line):
            char = line[idx]
            if char not in decors:
                text.write(char)
            else:
                # end current text node
                if len(text.getvalue()) > 0:
                    output['content'].append({
                        'type': None,
                        'tag': None,
                        'content': text.getvalue(),
                    })

                # parse decoration node
                decorations, seek = self._parse_decoration(line, seek=idx)
                output['content'] += decorations
                if seek is not None:
                    idx = seek
                    text.close()
                    text = StringBuilder()
                else:
                    break

            idx += 1

        if len(text.getvalue()) > 0:
            output['content'].append({
                'content': text.getvalue(),
                'tag': None,
                'type': None,
            })

        return output

    def _parse_paragraph(self, line):
        return {
            'type': 'paragraph',
            'tag': 'p',
            'content': [self._parse_text(line)],
        }
