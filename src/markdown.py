import re
import json
from pprint import pformat
from collections import namedtuple

import utils
from constants import tokens as tks
from errors import ParsingException


Decoration = namedtuple('Decoration', ['idx', 'char'])


class Markdown:
    def __init__(self, filename):
        self._filename = filename
        self._lineno = 0

        # output JSON
        self._output = {
            'file': filename,
            'content': [],
        }

    def __repr__(self):
        return f'File {self._filename} - Lines processed {self._lineno}'

    def __str__(self):
        return pformat(self._output)

    def dump(self):
        return json.dump(self._output)

    def dumps(self):
        return json.dumps(self._output)

    def parse(self):
        reader = utils.read_file(self._filename)
        while (line := next(reader, None)):
            if re.match(tks['header'], line):
                header = self._parse_header(line)
                self._append(header)
            elif re.match(tks['blockquote'], line):
                blockquote = self._parse_blockquote(line)
                self._append(blockquote)
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

        return self._output

    def _append(self, val):
        self._output['content'].append(val)

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
        if len(meatch) > 1:
            raise ParsingException(self._file, self._lineno, '')
        elif len(meatch) < 1:
            raise ParsingException(self._file, self._lineno, '')

        blockquote, content = match[0]
        return {
            'token': 'blockquote',
            'tag': 'blockquote',
            'content': content,
        }

    def _parse_image(self, line):
        pass

    def _parse_codeblock(self, line):
        match = re.findall(tks['codeblock'], line)
        if len(meatch) > 1:
            raise ParsingException(self._file, self._lineno, '')
        elif len(meatch) < 1:
            raise ParsingException(self._file, self._lineno, '')

        blockquote, content = match[0]
        return {
            'token': 'blockquote',
            'tag': 'blockquote',
            'content': content,
        }

        pass

    def _parse_link(self, line, seek=0):
        pass

    def _parse_text(self, line):
        decor_stack = []
        decor_tokens = set(
            '*', # bold
            '_', # underline
            '~', # strikethrough
            '/', # italics
            '`', # code
            '[', # link
        )

        result = {
            'element': 'paragraph',
            'tag': 'p',
            'content': [],
        }

        idx = 0
        while idx < len(line):
            char = line[idx]
            if char in decor_tokens:
                # if char == decor_stack[-1].char
                #     decor = decor_stack.pop()
                #     result['content'].append()

                if char == '[':
                    # TODO: figure out how to jump idx
                    # TODO: figure out how to append result
                    # self._parse_link(line, idx)
                    pass
                else:
                    decor_stack.append(Decoration(idx, char))





