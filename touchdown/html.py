import pdb
from pprint import pprint


class Html:
    def __init__(self, md_tokens):
        self._md_tokens = md_tokens
        self._content = None

    def __iter__(self):
        self._contents = iter(self._md_tokens['content'])
        return self

    def __next__(self):
        token = next(self._contents, None)
        if not token:
            raise StopIteration

        if token['type'] == 'header':
            return self._write_header(token)
        elif token['type'] == 'blockquote':
            return self._write_blockquote(token)
        elif token['type'] == 'image':
            return self._write_image(token)
        elif token['type'] == 'ordered_list' or token['type'] == 'unordered_list':
            return self._write_list(token)
        elif token['type'] == 'paragraph':
            return self._write_paragraph(token)
        elif token['type'] == 'codeblock':
            return self._write_codeblock(token)

    def interpret(self):
        html = '\n'.join([element for element in self])
        return html

    def _write_header(self, token):
        tag = token['tag']
        content = token['content']
        text = self._write_text(content)
        return f'<{tag}>{text}</{tag}>'

    def _write_blockquote(self, token):
        tag = token['tag']
        content = token['content']
        text = self._write_text(content)
        return f'<{tag}>{text}</{tag}>'

    def _write_codeblock(self, token):
        tag = token['tag']
        language = token['language']
        content = ''.join(token['content'])
        if language is None:
            return f'<{tag}>\n{content}\n</{tag}>'
        else:
            return f'<{tag} data-language="{language}">\n{content}\n</{tag}>'

    def _write_list(self, elem):
        tag = elem['tag']
        content = elem['content']
        list_items = '\n'.join([
            f'\t<li>{self._write_text(li["content"])}</li>'
            for li in content
        ])
        return f'<{tag}>\n{list_items}\n</{tag}>'

    def _write_paragraph(self, token):
        tag = token['tag']
        text = ''.join([
            self._write_text(line)
            for line in token['content']
        ])

        # trim any white space at the beginning or end of the text block
        text = text.strip()

        if text == '':
            # we want to avoid adding paragraph tags with no text inbetween.
            # if the interpreter ever gets to this state, we return an empty string because
            # the empty string will be parsed out inside `interpret()` after we call `''.join()`
            # to combine the html together
            return ''

        return f'<{tag}>{text}</{tag}>'

    def _write_text(self, token):
        text = []
        for text_block in token['content']:
            tags = text_block.get('tag', None)
            content = text_block['content']
            if content == '\n':
                # this if statement will skip over text blocks that only newlines.
                # we append an empty string because empty strings are parsed out
                # when we call `''.join()` at the end of the function
                text.append('')
            elif tags is None:
                # an empty tag means that the `content` is not wrapped in bold, underline,
                # italic, code, strikethrough, etc. rather the text_block is just plain
                # text
                text.append(content)
            else:
                # in the event there are tags, we need to wrap the `content` of the
                # text block with the open and closed tags
                open_tags = ''.join([ f'<{tag}>' for tag in tags ])
                close_tags = ''.join([ f'</{tag}>' for tag in reversed(tags) ])
                text.append(f'{open_tags}{content}{close_tags}')

        return ''.join(text)
