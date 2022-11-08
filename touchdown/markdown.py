import re
import pdb
from io import StringIO as StringBuilder
from pprint import pprint
from pathlib import Path
from urllib.parse import urlparse, ParseResult

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
        return self._parse(line)

    @property
    def markdown(self):
        head = []
        body = []
        for token in self:
            if token is None:
                continue

            page_tag = token.pop('page_tag', None)
            if page_tag == 'head':
                head.append(token)
            elif page_tag is None or page_tag == 'body':
                body.append(token)

        return {
            'filename': self._filepath.name,
            'head': head if len(head) > 0 else None,
            'body': body if len(body) > 0 else None,
        }

    def _parse(self, line):
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
        elif re.match(MARKDOWN_REGEXS['mathblock'], line):
            return self._parse_mathblock(self._reader)
        elif re.match(MARKDOWN_REGEXS['import'], line):
            return self._parse_import(line)
        elif len(line) >= 1 and line[0] == '<':
            return self._parse_web_component(self._reader)
        elif re.match(MARKDOWN_REGEXS['paragraph_id'], line):
            return self._parse_paragraph(line, includes_id=True)
        else:
            return self._parse_paragraph(line)

    def _parse_header(self, line, includes_id=False):
        match = re.findall(MARKDOWN_REGEXS['header_id'], line) \
            if includes_id \
            else re.findall(MARKDOWN_REGEXS['header'], line)

        # Check for syntax errors
        # 1. raise error if a header with an ID is incorrectly formatted
        # 2. raise error if a regular header is incorrectly formatted
        if includes_id and len(match) != 1 and len(match[0]) != 3:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')
        elif not includes_id and len(match) != 1 and len(match[0]) != 2:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        # get header content and parse inner text
        header = match[0][0]
        text_token = self._parse_text(match[0][-1])

        # need to join all the actual text in the header node
        # before generating an ID
        header_id_text = ''.join([
            token['content']
            for token in text_token['content']
        ])
        header_id = create_html_tag_id(header_id_text)

        return {
            'page_tag': 'body',
            'id': header_id,
            'type': 'header',
            'tag': f'h{len(header)}',
            'content': text_token,
        }

    def _parse_blockquote(self, line):
        match = re.findall(MARKDOWN_REGEXS['blockquote'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        content = match[0]
        return {
            'page_tag': 'body',
            'type': 'blockquote',
            'tag': 'blockquote',
            'content': self._parse_text(content),
        }

    def _parse_mathblock(self, reader):
        content = []
        while (line := next(reader, None)):
            if re.findall(MARKDOWN_REGEXS['mathblock'], line):
                break
            else:
                content.append(line)

        mathblock = ''.join(content).strip()
        return {
            'page_tag': 'body',
            'type': 'mathblock',
            'tag': 'div',
            'content': f'\\[{mathblock}\\]'
        }

    def _parse_codeblock(self, reader):
        reader.backstep()
        codeblock_header = next(reader)
        match = re.findall(MARKDOWN_REGEXS['codeblock_header'], codeblock_header)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        language = match[0][1] \
            if match[0][1] != '' \
            else None

        content = []
        while (line := next(reader, None)):
            if re.findall(MARKDOWN_REGEXS['codeblock_footer'], line):
                break
            else:
                content.append(line)

        return {
            'page_tag': 'body',
            'type': 'codeblock',
            'tag': 'pre',
            'language': language,
            'content': ''.join(content).strip()
        }

    def _parse_import(self, line):
        if self._filepath.suffix == '.md':
            raise MarkdownSyntaxError(
                self._filepath,
                self._lineno,
                f'Trying to use `import` statement inside file with `.md` extension - try changing `{self._filepath}` extension to `.mdx`'
            )

        # Check for syntax errors
        # 1. check that the import statement is correctly formatted
        # 2 & 3. an import statement can only include `defer` OR `async, NOT BOTH
        # the last 2 checks ensure that the import statement is not `defer async import ...`
        match = re.findall(MARKDOWN_REGEXS['import'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')
        elif match[0][0] != '' and match[0][0] != 'async':
            raise MarkdownSyntaxError(
                self._filepath,
                self._lineno,
                f'Invalid import syntax - do not recognize `{match[0][0]}`'
            )
        elif match[0][1] != '' and match[0][1] != 'defer':
            raise MarkdownSyntaxError(
                self._filepath,
                self._lineno,
                f'Invalid import syntax - do not recognize `{match[0][1]}`'
            )

        # extract information from import statement
        is_async = match[0][0] == 'async'
        is_defer = match[0][1] == 'defer'

        # uri is a special case because a URI can either be a URL to a JS/CSS file
        # or it can be a local path to a a JS/CSS file on the user's machine
        #
        # TODO: It'd be a QoL functionality to throw a parsing error if the file
        # is not found on the local machine - it would save debugging within the browser
        uri = urlparse(match[0][2]) \
            if match[0][2][:4] == 'http' \
            else Path(match[0][2])

        # if the uri is a URL, it's possible for their to be query parameters after the file extension
        # we split at a `?` character if there is one to ensure we get no query parameters and just the
        # the file type
        is_url = type(uri) == ParseResult
        uri_suffix = uri.suffix \
            if not is_url \
            else f'.{uri.path.split(".")[-1]}'

        if uri_suffix not in set(['.js', '.css']):
            raise MarkdownSyntaxError(self._filepath, self._lineno, f'Trying to import unrecognized filetype `{uri_suffix}`')
        elif uri_suffix == '.css' and is_async:
            raise MarkdownSyntaxError(self._filepath, self._lineno, f'Cannot import css with `async` - try removing `async`')
        elif is_async and is_defer:
            raise MarkdownSyntaxError(
                self._filepath,
                self._lineno,
                f'Invalid import syntax - cannot use both `async` and `defer`'
            )

        if not is_url and uri.is_dir():
            return {
                'page_tag': 'head',
                'url': False,
                'type': 'import',
                'tag': 'script',
                'async': is_async,
                'defer': is_defer,
                'src': f'{uri}/index.js'
            }
        elif uri_suffix == '.css':
            return {
                'page_tag': 'head',
                'type': 'import',
                'tag': 'link',
                'url': is_url,
                'href': uri.geturl() if is_url else str(uri),
                'rel': 'preload' if is_defer else 'stylesheet',
            }
        elif uri_suffix == '.js':
            return {
                'page_tag': 'head',
                'type': 'import',
                'tag': 'script',
                'url': is_url,
                'async': is_async,
                'defer': is_defer,
                'src': uri.geturl() if is_url else str(uri),
            }

    def _parse_list(self, reader, list_type, list_tag):
        reader.backstep() # reset the file generator back to the beginning of the ordered list

        output = {
            'page_tag': 'body',
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

    def _parse_web_component(self, reader):
        reader.backstep()

        tag = None
        content = None
        builder = StringBuilder()
        while (line := next(reader, None)):

            builder.write(line)
            if re.match(MARKDOWN_REGEXS['web_component'], builder.getvalue()):
                match = re.findall(MARKDOWN_REGEXS['web_component'], builder.getvalue())[0]
                content = match[0]
                tag = match[1]
                break

        if content is None:
            raise MarkdownSyntaxError(self._filepath, self._lineno, 'Could not find closing tag to web component')

        return {
            'page_tag': 'body',
            'type': 'web_component',
            'tag': tag,
            'content': content,
        }


    def _parse_image(self, line):
        match = re.findall(MARKDOWN_REGEXS['image'], line)
        if len(match) != 1:
            raise MarkdownSyntaxError(self._filepath, self._lineno, '')

        alt_text, uri = match[0]
        return {
            'page_tag': 'body',
            'type': 'image',
            'tag': 'img',
            'uri': uri,
            'alt': alt_text,
        }

    def _extract_maths_from_text(self, line):
        maths_itr = re.finditer(MARKDOWN_REGEXS['math'], line)
        return [
            {
                'type': 'math',
                'tag': ['span'],
                'start': match.start(0),
                'end': match.end(0),
                'content': match.groups()[0],
            }
            for match in maths_itr
        ]

    def _parse_maths(self, line):
        maths = self._extract_maths_from_text(line)
        if len(maths) == 0:
            return [line]

        content = []
        idx = 0
        while idx < len(maths):
            curr = maths[idx]
            curr['content'] = f'\\({curr["content"]}\\)'

            start = None
            end = None
            if idx == 0:
                start = 0
                end = curr['start']
            else:
                start = content[-1]['end']
                end = curr['start']

            text = line[start:end]
            content.append(text)
            content.append(curr)
            idx += 1

        # after parsing all the math blocks, we need to append any lingering
        # text that might come afterwards
        last_text = line[content[-1]['end']:]
        content.append(last_text)

        # filter out any sub-text tokens that are just empty strings
        content = list(filter(lambda string: string != '', content))

        return content

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
    def _parse_links(self, text_tokens):
        i = 0
        while i < len(text_tokens):
            token = text_tokens[i]

            if token['type'] == 'math':
                i += 1
                continue

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

    def _parse_characters(self, line):
        builder = StringBuilder()
        content = []
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
                raise MarkdownSyntaxError(self._filepath, self._lineno, f'`{char}` needs a matching closing character')
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

        return list(filter(lambda token: token['content'] != '', content))

    def _parse_text(self, line):
        # must parse inline mathblocks first because these math blocks
        # contain math characters that are also include decoration characters
        math = self._parse_maths(line)

        # parse normal text and decorations and while parsing skip over
        # inline math nodes that have already been parsed
        math_text = []
        for token in math:
            if type(token) == str:
                math_text += self._parse_characters(token)
            else:
                # NOTE: we delete these unnecessary `start` and `end nodes
                # because they were requied through-out all of the `_parse_maths`
                del token['start']
                del token['end']
                math_text.append(token)

        # iterate over all the text nodes and split out links from text
        math_text_links = self._parse_links(math_text)

        return {
            'type': 'text',
            # filter out any text nodes that are just empty strings
            'content': list(filter(lambda token: token['content'] != '', math_text_links))
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
            'page_tag': 'body',
            'id': paragraph_id,
            'type': 'paragraph',
            'tag': 'p',
            'content': [self._parse_text(line)],
        }
