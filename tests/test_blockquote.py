import unittest
from pathlib import Path

from touchdown import markdown, html

TESTCASE_DIR = '../testcases/blockquote'

class TestBlockquote(unittest.TestCase):
    def test_multiple_blockquotes_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_multiple_blockquotes.md')
        assert False

    def test_multiple_blockquotes_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_multiple_blockquotes.md')
        assert False

    def test_single_blockquote_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_blockquotes.md')
        assert False

    def test_single_blockquote_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_blockquotes.md')
        assert False
