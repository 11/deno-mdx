import re
import json
import utils
import pdb

from pprint import pprint
from collections import namedtuple, OrderedDict
from constants import tokens as tks


# used as a way
Decoration = namedtuple('Decoration', ['idx', 'char'])


class Markdown:
    def __init__(self, filename):
        self._filename = filename
        self._output = {
            'file': filename,
            'content': [],
        }

    def __repr__(self):
        pass

    def __str__(self):
        return self.dumps()

    def dump(self):
        return json.dump(self._output)

    def dumps(self):
        return json.dumps(self._output)

    def parse(self):
        reader = utils.read_file(self._filename)
        for line in reader:
            if re.match(tks['header'], line):
                header = self._parse_header(line)
                self._append(header)
            elif re.match(tks['blockquote'], line):
                print('blockquote')
            elif re.match(tks['image'], line):
                print('image')
            elif re.match(tks['ordered_list'], line):
                print('ordered_list')
            elif re.match(tks['unordered_list'], line):
                print('unordered_list')
            elif re.match(tks['codeblock']['wrap'], line):
                print('codeblock')
            else:
                print('paragraph')

    def _append(self, val):
        if not val:
            # TODO: raise err
            pass

        self._output['content'].append(val)


    def _parse_header(self, line):
        match = re.findall(tks['header'], line)
        if len(match) > 1 or len(match) == 0:
            # TODO: raise err
            pass

        header, content = match[0]
        return {
            'token': 'header',
            'tag': f'h{len(header)}',
            'content': content,
        }


    def _parse_blockquote(self, line):
        pass

    def _parse_image(self, line):
        pass

    def _parse_codeblock(self, line):
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





