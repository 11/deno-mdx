import unittest
from pathlib import Path

from touchdown import markdown, html


TESTCASE_DIR = '../testcases/codeblock'


class TestHeader(unittest.TestCase):
    def test_codeblock_with_backticks_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_backticks.md')
        assert False

    def test_codeblock_with_backticks_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_backticks.md')
        assert False

    def test_codeblock_with_language_tag_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_language_tag.md')
        assert False

    def test_codeblock_with_language_tag_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_codeblock_with_language_tag.md')
        assert False

    def test_multiple_codeblocks_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_multiple_codeblocks.md')
        assert False

    def test_multiple_codeblocks_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_multiple_codeblocks.md')
        assert False

    def test_single_codeblock_multiline_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock_multiline.md')
        assert False

    def test_single_codeblock_multiline_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock_multiline.md')
        assert False

    def test_single_codeblock_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock.md')
        assert False

    def test_single_codeblock_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_codeblock.md')
        assert False
