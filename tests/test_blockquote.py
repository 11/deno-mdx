import unittest
from pathlib import Path
from pprint import pprint

from touchdown import markdown, html

TESTCASE_DIR = './testcases/blockquote'

class TestBlockquote(unittest.TestCase):
    def test_multiple_blockquotes_markdown(self):
        """ test that multiple blockquotes a line apart create their own separate blockquote tag """

        test_file = Path(f'{TESTCASE_DIR}/test_multiple_blockquotes.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": {
                        "content": [
                            {
                                "content": "Lorem ipsum dolor sit amet, "
                                "consectetur adipiscing "
                                "elit, sed do eiusmod tempor "
                                "incididunt ut labore et "
                                "dolore magna aliqua.",
                                "tag": None,
                                "type": None,
                            }
                        ],
                        "type": "text",
                    },
                    "tag": "blockquote",
                    "type": "blockquote",
                },
                {
                    "content": {
                        "content": [
                            {
                                "content": "Ut enim ad minim veniam, "
                                "quis nostrud exercitation "
                                "ullamco laboris nisi ut "
                                "aliquip ex ea commodo "
                                "consequat.",
                                "tag": None,
                                "type": None,
                            }
                        ],
                        "type": "text",
                    },
                    "tag": "blockquote",
                    "type": "blockquote",
                },
                {
                    "content": {
                        "content": [
                            {
                                "content": "Duis aute irure dolor in "
                                "reprehenderit in voluptate "
                                "velit esse cillum dolore eu "
                                "fugiat nulla pariatur.",
                                "tag": None,
                                "type": None,
                            }
                        ],
                        "type": "text",
                    },
                    "tag": "blockquote",
                    "type": "blockquote",
                },
            ],
            "filename": "test_multiple_blockquotes.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_multiple_blockquotes_html(self):
        """ test that multiple blockquotes a line apart create their own separate blockquote tag """

        test_file = Path(f'{TESTCASE_DIR}/test_multiple_blockquotes.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<blockquote>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</blockquote>\n' \
            '<blockquote>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</blockquote>\n' \
            '<blockquote>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</blockquote>\n' \
            '</body>\n' \
            '</html>'
        assert html(test_file) == expected_html

    def test_single_blockquote_markdown(self):
        """ sanity check that a single blockquote works """

        test_file = Path(f'{TESTCASE_DIR}/test_single_blockquote.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": {
                        "content": [
                            {
                                "content": "Lorem ipsum dolor sit amet, "
                                "consectetur adipiscing "
                                "elit, sed do eiusmod tempor "
                                "incididunt ut labore et "
                                "dolore magna aliqua. ",
                                "tag": None,
                                "type": None,
                            }
                        ],
                        "type": "text",
                    },
                    "tag": "blockquote",
                    "type": "blockquote",
                }
            ],
            "filename": "test_single_blockquote.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_single_blockquote_html(self):
        """ sanity check that a single blockquote works """

        test_file = Path(f'{TESTCASE_DIR}/test_single_blockquote.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<blockquote>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </blockquote>\n' \
            '</body>\n' \
            '</html>'
        assert html(test_file) == expected_html

    def test_merge_blockquotes_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_merge_blockquotes.md')
        assert False

    def test_merge_blockquotes_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_merge_blockquotes.md')
        assert False
