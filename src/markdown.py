import re
import json
from pprint import pformat
from collections import namedtuple

import utils
from constants import tokens as tks
from errors import ParsingException


Decoration = namedtuple('Decoration', ['idx', 'char'])


class Markdown:
    def __init__(self, filepath):
        self._filepath = filepath
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
                # self._append(header)
            elif re.match(tks['blockquote'], line):
                blockquote = self._parse_blockquote(line)
                yield blockquote
                # self._append(blockquote)
            elif re.match(tks['image'], line):
                print('image')
            elif re.match(tks['ordered_list'], line):
                print('ordered_list')
            elif re.match(tks['unordered_list'], line):
                print('unordered_list')
            elif re.match(tks['codeblock']['wrap'], reader):
                print('codeblock')
            else:
                print('paragraph')

            self._lineno += 1

        return self._output

    def dump(self):
        return json.dump(self.parse())

    def dumps(self):
        return json.dumps(self.parse())

    def parse(self):
        return {
            'filename': self._filepath.name,
            'filepath': self._filepath
            'content': [token for token in self],
        }

    def _parse_header(self, line):
        match = re.findall(tks['header'], line)
        if len(match) > 1:
            raise ParsingException(self._file, self._lineno, '')
        elif len(match) < 1:
            raise ParsingException(self._file, self._lineno, '')

        header, content = match[0]
        return {
            'token': 'header',
            'tag': f'h{len(header)}',
            'content': content,
        }

    def _parse_blockquote(self, line):
        match = re.findall(tks['blockquote'], line)
        if len(match) > 1:
            raise ParsingException(self._file, self._lineno, '')
        elif len(match) < 1:
            raise ParsingException(self._file, self._lineno, '')

        blockquote, content = match[0]
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
            raise ParsingException(self._file, self._lineno, '')
        elif len(match) < 1:
            raise ParsingException(self._file, self._lineno, '')

        codeblock, content = match[0]
        return {
            'token': 'codeblock',
            'tag': 'pre',
            'content': content,
        }

        pass

    def _parse_link(self, line, seek=0):
        pass

    def _parse_decoration(self, line, seek=0):
        pass

    def _parse_text(self, line):
        output = {
            'element': 'paragraph',
            'tag': 'p',
            'content': [],
        }

        decor_tks = set('*', '_', '~', '/', '`', '[')

        start = 0
        end = 0
        while end < len(line):
            cur = line[idx]
            prev = line[idx-1] if idx > 0 else 0

            if prev != '\\' and cur in decor_tks:
                # store plain text
                output['contnet'].append({
                    'element': 'text',
                    'content': line[start:end]
                })
                start = end

                # parse text decoration or link
                if cur == '[':
                    link = self._parse_link(self, line, idx)
                    output['content'].append(link)
                else:
                    decor = self._parse_decoration(self, line, idx);
                    output['content'].append(decor)

            end += 1

        return output

