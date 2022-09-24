import re
import pdb
from pathlib import Path
from io import StringIO as StringBuilder

from .errors import MarkdownSyntaxError
from .constants import SPECIAL_CHARS, MARKDOWN_REGEXS
from .utils.file import readfile
from .utils.parser import (
    lookahead,
    create_html_tag_id,
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
        # class variables
        self._filepath = Path(file)
        self._lineno = 0
        self._reader = None

        # properties 
        self._markdown = self.run()

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

        if re.match(MARKDOWN_REGEXS['header_id'], line):
            return self._parse_header(line, includes_id=True)
        elif re.match(MARKDOWN_REGEXS['header'], line):
            return self._parse_header(line)
        elif re.match(MARKDOWN_REGEXS['blockquote'], line):
            return self._parse_blockquote(line)
        elif re.match(MARKDOWN_REGEXS['ordered_list'], line):
            return self._parse_ordered_list(self._reader)
        elif re.match(MARKDOWN_REGEXS['unordered_list'], line):
            return self._parse_unordered_list(self._reader)
        elif re.match(MARKDOWN_REGEXS['image'], line):
            return self._parse_image(line)
        elif re.match(MARKDOWN_REGEXS['codeblock_header'], line):
            return self._parse_codeblock(self._reader)
        elif re.match(MARKDOWN_REGEXS['paragraph_id'], line):
            return self._parse_paragraph(line, includes_id=True)
        else:
            return self._parse_paragraph(line)

    @property
    def markdown(self):
        return self._markdown

    def run(self):
        markdown = {
            'filename': self._filepath.name,
            'content': [
                token 
                for token in self 
                if token is not None
            ],
        }

        return markdown

    def _parse_header(self, line, includes_id=False):
        match = re.findall(MARKDOWN_REGEXS['header_id'], line) \
            if includes_id \
            else re.findall(MARKDOWN_REGEXS['header'], line)

        if includes_id and len(match) != 1 and len(match[0]) != 3:
            # raising error if a header with an ID is incorrectly formatted
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')
        elif not includes_id and len(match) != 1 and len(match[0]) != 2:
            # raising error if a header is incorrectly formatted
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        header = match[0][0]
        header_id = create_html_tag_id(match[0][1])
        content = match[0][-1]

        return {
            'id': header_id,
            'type': 'header',
            'tag': f'h{len(header)}',
            'content': self._parse_text(content),
        }

    def _parse_blockquote(self, line):
        match = re.findall(MARKDOWN_REGEXS['blockquote'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        content = match[0]
        return {
            'type': 'blockquote',
            'tag': 'blockquote',
            'content': self._parse_text(content),
        }

    def _parse_codeblock(self, reader):
        output = {
            'type': 'codeblock',
            'tag': 'pre',
            'language': None,
            'content': [],
        }

        reader.backstep()
        codeblock_header = next(reader)
        match = re.findall(MARKDOWN_REGEXS['codeblock_header'], codeblock_header)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        _, language = match[0]
        if language != '':
            output['language'] = language

        while (line := next(reader, None)):
            if re.findall(MARKDOWN_REGEXS['codeblock_footer'], line):
                break
            else:
                output['content'].append(line)

        return output

    def _parse_list(self, reader, list_type, list_tag):
        reader.backstep() # reset the file generator back to the beginning of the ordered list

        output = {
            'type': list_type,
            'tag': list_tag,
            'content': [],
        }

        while (line := next(reader, None)):
            match = None
            if list_type == 'ordered_list' and re.match(MARKDOWN_REGEXS['ordered_list'], line):
                match = re.findall(MARKDOWN_REGEXS['ordered_list'], line)
            elif list_type == 'unordered_list' and re.match(MARKDOWN_REGEXS['unordered_list'], line):
                match = re.findall(MARKDOWN_REGEXS['unordered_list'], line)
            else:
                reader.backstep()
                break

            if len(match) != 1:
                raise MarkdownSyntaxError(self._filepath, self._lineno, '')

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
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        uri, alt_text = match[0]
        return {
            'type': 'image',
            'tag': 'img',
            'url': uri,
            'alt': alt_text,
        }

    # TODO: WORKS BUT COULD BE BETTER
    # make this function return the links and the indices of the substrings
    # that are inbetween the links
    def _extract_links_from_text(self, text_token):
        # iterator that iterates over a line of text and looks for the next
        # start and end index of a link
        link_itr = re.finditer(MARKDOWN_REGEXS['link'], text_token['content'])

        # return relevant link info
        return [
            {
                'type': 'link',
                'tag': ['a'],
                'start': match.start(0),
                'end': match.end(0),
                'content': match.groups()[0],
                'href': match.groups()[1],
            }
            for match in link_itr
        ]

    # TODO: WORKS BUT COULD BE BETTER
    def _parse_link(self, text_tokens):
        i = 0
        while i < len(text_tokens):
            token = text_tokens[i]
            link_ranges = self._extract_links_from_text(token)

            j = 0

            line = None
            start = None
            end = None
            subcontent = []
            while j < len(link_ranges):
                line = token['content']

                link_range = link_ranges[j]
                start = link_range['start']
                end = link_range['end']

                if j == 0:
                    before = token.copy()
                    before['content'] = line[:start]

                    link = link_range.copy()
                    link['tag'] += [] if before['tag'] is None else before['tag']
                    del link['start']
                    del link['end']

                    subcontent += [before, link]
                else:
                    prev_range_end = link_ranges[j-1]['end']

                    before = token.copy()
                    before['content'] = line[prev_range_end:start]

                    link = link_range.copy()
                    link['tag'] += [] if before['tag'] is None else before['tag']
                    del link['start']
                    del link['end']

                    subcontent += [before, link]

                j += 1

            if len(subcontent) > 0:
                # append any potential text that comes after the last link
                last = token.copy()
                last['content'] = line[end:]
                subcontent.append(last)

                prev = text_tokens[:i]
                curr = subcontent
                post = text_tokens[i+1:]
                text_tokens = prev + curr + post
                i += len(subcontent)
            else:
                i += 1

        return text_tokens

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

            if not (idx < len(line) and len(active) > 0):
                # this loop HAS to run 1 extra iteration to know that we've reached the end 
                # of the line, or to process any unclosed special characters. because of 
                # this, we subtract 1 to return the correct index to seek to in `_parse_text`
                idx -= 1

                break

        if len(active) > 0:
            # if the entire line of text was parsed and there are missing
            # closing decoration characters, raise a syntax error
            active_decorations = list(active)
            raise MarkdownSyntaxError(self._filepath, self._lineno, f'{active_decorations[0]} needs a matching closing character')

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
                raise MarkdownSyntaxError(self._filepath, self._lineno, f'{char} needs a matching closing character')
            elif char in SPECIAL_CHARS and lag != '\\' and lookahead(char, line[idx+1:]):
                # if reading a special character that isn't escaped and
                # the rest of the string contains a closing character,
                # start parsing deocrations
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

        content = list(filter(lambda token: token['content'] != '', content))
        content = self._parse_link(content)
        return {
            'type': 'text',
            'content': content,
        }

    def _parse_paragraph(self, line, includes_id=False):
        # check if the line only contains a newline character. if so we
        # do nothing and return None
        if line == '\n':
            return None

        # check if the paragraph begins with an ID. if so, parse out the id
        # before parsing text
        paragraph_id = None
        if includes_id:
            # grab the paragraph ID
            match = re.findall(MARKDOWN_REGEXS['paragraph_id'], line)
            if len(match) != 1:
                raise MarkdownSyntaxError(self._filepath, self._lineno, '')
            paragraph_id = match[0]

            # advance the line foward past the ID
            seek = line.find('}') + 1
            line = line[seek:].lstrip()

        return {
            'id': paragraph_id,
            'type': 'paragraph',
            'tag': 'p',
            'content': [self._parse_text(line)],
        }
