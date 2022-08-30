import pdb


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

    def interpret(self):
        html = '\n'.join([element for element in self])
        return html

    def _write_header(self, elem):
        tag = elem['tag']
        content = elem['content']
        text = self._write_text(content)
        return f'<{tag}>{text}</{tag}>'

    def _write_blockquote(self, elem):
        tag = elem['tag']
        content = elem['content']
        text = self._write_text(content)
        return f'<{tag}>{text}</{tag}>'

    def _write_codeblock(self, elem):
        tag = elem['tag']
        content = elem['content']
        language = elem['language']
        return f'<{tag} data-language="{language}">{content}</{tag}>'

    def _write_list(self, elem):
        tag = elem['tag']
        content = elem['content']
        list_items = [
            f'<li>{self._write_text(li["content"])}</li>'
            for li in content
        ]
        return f'<{tag}>{"".join(list_items)}</{tag}>'

    def _write_paragraph(self, elem):
        tag = elem['tag']
        content = elem['content']
        text = self._write_text(content)
        return f'<{tag}>{text}</{tag}>'

    def _write_text(self, text):
        lines = []
        for line in text:
            for block in line['content']:
                if block.get('tag', None) is None:
                    lines.append(block['content'])
                else:
                    start = [f'<{tag}>' for tag in block['tag']]
                    end = reversed([f'</{tag}>' for tag in block['tag']])
                    substr = f'{"".join(start)}{block["content"]}{"".join(end)}'
                    lines.append(substr)

        return ''.join(lines)
