import unittest
from pathlib import Path
from pprint import pprint

from touchdown import markdown, html


TESTCASE_DIR = './testcases/mathblock'


class TestMathblock(unittest.TestCase):
    def test_single_mathblock_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_mathblock.md')
        expected_markdown = {
            'head': None,
            'body': [{
                'content': '\\[\\sqrt{3x-1}+(1+x)^2\\]',
                'tag': 'div',
                'type': 'mathblock'
                }],
            'filename': 'test_single_mathblock.md'
        }
        assert markdown(test_file) == expected_markdown

    def test_single_mathblock_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_mathblock.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<div>\\[\\sqrt{3x-1}+(1+x)^2\\]</div>\n' \
            '</body>\n' \
            '</html>'
        assert html(test_file) == expected_html
