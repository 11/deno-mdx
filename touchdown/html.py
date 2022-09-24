class Html:
    def __init__(self, md_tokens):
        # class variables
        self._md_tokens = md_tokens
        self._content = None

        # properties
        self._html = self.run()

    def __iter__(self):
        self._content = iter(self._md_tokens['content'])
        return self

    def __next__(self):
        token = next(self._content, None)
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

    def run(self):
        html = '\n'.join([element for element in self])
        return html

    @property
    def html(self):
        return self._html

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
        paragraph_id = token['id']
        line = ''.join([
            self._write_text(text)
            for text in token['content']
        ])

        # trim any white space at the beginning or end of the text block
        line = line.strip()

        if line == '':
            # we want to avoid adding paragraph tags with no text inbetween.
            # if the interpreter ever gets to this state, we return an empty string because
            # the empty string will be removed inside `interpret()` after we call `''.join()`
            # to combine the html together
            # -- TODO: try just returning None
            return ''

        if paragraph_id:
            return f'<{tag} id="{paragraph_id}">{line}</{tag}>'

        return f'<{tag}>{line}</{tag}>'

    def _write_text(self, token):
        text = []
        for text_block in token['content']:
            tags = text_block.get('tag', None)
            token = text_block['type']
            content = text_block['content']
            if content == '\n':
                # this if statement will skip over text blocks that only contain newlines.
                continue
            elif token == 'link':
                link = self._write_link(text_block)
                text.append(link)
            elif tags is None:
                # an empty `tags` list means that the `content` is not wrapped in bold, underline,
                # italic, code, strikethrough, etc. thus the `text_block` is just plain text
                text.append(content)
            else:
                # sort the list of tags to ensure the output HTML is always consistent
                tags = sorted(tags)

                # in the event there are tags, we need to wrap the `content` of the
                # text block with the open and closed tags
                open_tags = ''.join([ f'<{tag}>' for tag in tags ])
                close_tags = ''.join([ f'</{tag}>' for tag in reversed(tags) ])
                text.append(f'{open_tags}{content}{close_tags}')

        return ''.join(text)

    def _write_link(self, token):
        tags = list(filter(lambda tag: tag != 'a', token['tag']))
        open_tags = ''.join([ f'<{tag}>' for tag in tags ])
        close_tags = ''.join([ f'</{tag}>' for tag in reversed(tags) ])

        content = token['content']
        href = '#' \
            if token['href'] == '' \
            else token['href']

        return f'{open_tags}<a href="{href}">{content}</a>{close_tags}'
