import unittest
from pprint import pprint
from pathlib import Path

from touchdown import markdown, html


TESTCASE_DIR = './testcases/codeblock'


class TestCodeblock(unittest.TestCase):
    def test_codeblock_with_backticks_markdown(self):
        """ test that backticks aren't incorrectly mistaken for a codeblock start/end symbol """

        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_backticks.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": "function greet(name) {\n"
                    "    console.log(`Hello ${name}`)\n"
                    "}",
                    "language": "javascript",
                    "tag": "pre",
                    "type": "codeblock",
                }
            ],
            "filename": "test_codeblock_with_backticks.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_codeblock_with_backticks_html(self):
        """ test that backticks aren't incorrectly mistaken for a codeblock start/end symbol """

        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_backticks.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<pre data-language="javascript">\n' \
            'function greet(name) {\n' \
            '    console.log(`Hello ${name}`)\n' \
            '}\n' \
            '</pre>\n' \
            '</body>\n' \
            '</html>'
        assert html(test_file) == expected_html

    def test_codeblock_with_language_tag_markdown(self):
        """ test the language tag is parsed and included as metadata """

        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_language_tag.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": "console.log('hello world')\n"
                    "\n"
                    "function add(a, b) {\n"
                    "    return a + b\n"
                    "}",
                    "language": "javascript",
                    "tag": "pre",
                    "type": "codeblock",
                }
            ],
            "filename": "test_codeblock_with_language_tag.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_codeblock_with_language_tag_html(self):
        """ test the language tag is parsed and included as metadata """

        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_language_tag.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<pre data-language="javascript">\n' \
            'console.log(\'hello world\')\n' \
            '\n' \
            'function add(a, b) {\n' \
            '    return a + b\n' \
            '}\n' \
            '</pre>\n' \
            '</body>\n' \
            '</html>'
        assert html(test_file) == expected_html

    def test_multiple_codeblocks_markdown(self):
        """ test that two codewblocks next to eachother are parsed correctly """

        test_file = Path(f'{TESTCASE_DIR}/test_multiple_codeblocks.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": "console.log('line 1')\n"
                    "console.log('line 2')\n"
                    "console.log('line 3')\n"
                    "console.log('line 4')",
                    "language": None,
                    "tag": "pre",
                    "type": "codeblock",
                },
                {
                    "content": "console.log('line 5')\n"
                    "console.log('line 6')\n"
                    "console.log('line 7')\n"
                    "console.log('line 8')",
                    "language": None,
                    "tag": "pre",
                    "type": "codeblock",
                },
            ],
            "filename": "test_multiple_codeblocks.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_multiple_codeblocks_html(self):
        """ test that two codewblocks next to eachother are parsed correctly """

        test_file = Path(f'{TESTCASE_DIR}/test_multiple_codeblocks.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<pre>\n' \
            'console.log(\'line 1\')\n' \
            'console.log(\'line 2\')\n' \
            'console.log(\'line 3\')\n' \
            'console.log(\'line 4\')\n' \
            '</pre>\n' \
            '<pre>\n' \
            'console.log(\'line 5\')\n' \
            'console.log(\'line 6\')\n' \
            'console.log(\'line 7\')\n' \
            'console.log(\'line 8\')\n' \
            '</pre>\n' \
            '</body>\n' \
            '</html>'

        assert html(test_file) == expected_html

    def test_single_codeblock_markdown(self):
        """ sanity check that a basic codeblock is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": "console.log('hello world')",
                    "language": None,
                    "tag": "pre",
                    "type": "codeblock",
                }
            ],
            "filename": "test_single_codeblock.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_single_codeblock_html(self):
        """ sanity check that a basic codeblock is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<pre>\n' \
            'console.log(\'hello world\')\n' \
            '</pre>\n' \
            '</body>\n' \
            '</html>'

        assert html(test_file) == expected_html

    def test_single_codeblock_multiline_markdown(self):
        """ testing that multiple lines of code are contained within a codeblock """

        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock_multiline.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": "console.log('line 1')\n"
                    "console.log('line 2')\n"
                    "console.log('line 3')\n"
                    "console.log('line 4')",
                    "language": None,
                    "tag": "pre",
                    "type": "codeblock",
                }
            ],
            "filename": "test_single_codeblock_multiline.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_single_codeblock_multiline_html(self):
        """ testing that multiple lines of code are contained within a codeblock """

        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock_multiline.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<pre>\n' \
            'console.log(\'line 1\')\n' \
            'console.log(\'line 2\')\n' \
            'console.log(\'line 3\')\n' \
            'console.log(\'line 4\')\n' \
            '</pre>\n' \
            '</body>\n' \
            '</html>'

        assert html(test_file) == expected_html
