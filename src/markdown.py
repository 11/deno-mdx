import re
import json
from pprint import pformat
from pathlib import Path

import utils
from constants import tokens as tks
from errors import MarkdownSyntaxError


class Markdown:
    def __init__(self, file):
        self._filepath = Path(file)
        self._filename = filepath.name
        self._lineno = 0

    def __repr__(self):
        return f'File {self._filename} - Lines processed {self._lineno}'

    def __str__(self):
        return pformat(self.parse())

    def __next__(self):
        reader = utils.read_file(self._filename)
        while (line := next(reader, None)):
            if re.match(tks['header'], line):
                header = self._parse_header(line)
                yield header
            elif re.match(tks['blockquote'], line):
                blockquote = self._parse_blockquote(line)
                yield blockquote
            elif re.match(tks['ordered_list'], line):
                ordered_list = self._parse_ordered_list(reader)
                yield ordered_list
            elif re.match(tks['unordered_list'], line):
                unordered_list = self._parse_unordered_list(reader)
                yield unordered_list
            elif re.match(tks['image'], line):
                print('image')
            elif re.match(tks['codeblock'], reader):
                print('codeblock')
            else:
                print('paragraph')

            self._lineno += 1

    def dump(self):
        return json.dump(self.parse())

    def parse(self):
        if not self._filepath:
            raise FileNotFoundError

        return {
            'filename': self._filepath.name,
            'filepath': self._filepath,
            'content': [token for token in self],
        }

    def _parse_header(self, line):
        match = re.findall(tks['header'], line)
        if len(match) > 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')
        elif len(match) < 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        header, content = match[0]
        if not header or not content:
            return None

        return {
            'token': 'header',
            'tag': f'h{len(header)}',
            'content': content,
        }

    def _parse_blockquote(self, line):
        match = re.findall(tks['blockquote'], line)
        if len(match) > 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')
        elif len(match) < 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        blockquote, content = match[0]
        if not blockquote or not content:
            return None

        return {
            'token': 'blockquote',
            'tag': 'blockquote',
            'content': content,
        }

    def _parse_image(self, line):
        pass


    def _parse_codeblock(self, line, reader):
        match = re.findall(tks['codeblock'], line)
        if len(match) > 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')
        elif len(match) < 1:
            raise MarkdownSyntaxError(self._file, self._lineno, '')

        codeblock, content = match[0]
        if not codeblock or not content:
            return None

        return {
            'token': 'codeblock',
            'tag': 'pre',
            'content': content,
        }

    def _parse_list(self, reader, list_type, list_tag):
        # reset the file generator back to the beginning of the ordered list
        reader.backstep()

        output = {
            'element': list_type,
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

            if len(match) > 1 or len(match < 1):
                raise MarkdownSyntaxError(self._file, self._lineno, '')

            _, content = match[0]
            output['content'].append({
                'token': 'listitem',
                'tag': 'li',
                'content': content,
            })

        return output

    def _parse_ordered_list(self, reader):
        return self._parse_list(reader, 'ordered_list', 'ol')

    def _parse_unordered_list(self, line):
        return self._parse_list(reader, 'unordered_list', 'ul')

    def _parse_link(self, line, seek=0):
        pass

    def _parse_decoration(self, line, seek=0):
        pass

    def _parse_text(self, line):
        if not line:
            return None

        output = { 'element': 'paragraph', 'tag': 'p', 'content': [], }
        decors = set('*', '_', '~', '/', '`', '[')

        start = 0
        end = 0
        while end < len(line):
            cur = line[idx]
            prev = line[idx-1] if idx > 0 else 0

            if prev != '\\' and cur in decors:
                # append plain text to output and reset sliding window
                text = { 'element': 'text', 'content': line[start:end] }
                output['content'].append(text)
                start = end

                if cur == '[':
                    link = self._parse_link(self, line, idx)
                    output['content'].append(link)
                else:
                    decor = self._parse_decoration(self, line, idx);
                    output['content'].append(decor)

            end += 1

        return output

