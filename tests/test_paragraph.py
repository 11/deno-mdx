import unittest
from pathlib import Path
from pprint import pprint

from touchdown import to_ast, to_html


TESTCASE_DIR = './testcases/paragraph'


class TestParagraph(unittest.TestCase):
    def test_paragraph_with_id_markdown(self):
        """ sanity check that IDs can be added to the beginning of a paragraph """

        test_file = Path(f'{TESTCASE_DIR}/test_paragraph_with_id.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Lorem ipsum dolor sit "
                                    "amet, consectetur "
                                    "adipiscing elit, sed do "
                                    "eiusmod tempor incididunt "
                                    "ut labore et dolore magna "
                                    "aliqua.\n",
                                    "tag": None,
                                    "type": None,
                                }
                            ],
                            "type": "text",
                        }
                    ],
                    "id": "lorem-ipsum",
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_paragraph_with_id.md",
        }
        assert to_ast(test_file) == expected_markdown

    def test_paragraph_with_id_html(self):
        """ sanity check that IDs can be added to the beginning of a paragraph """

        test_file = Path(f'{TESTCASE_DIR}/test_paragraph_with_id.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<p id="lorem-ipsum">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_id_paragraph_with_invalid_characters_in_id_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_id_paragraph_with_invalid_characters_in_id.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "{^lorem-ipsum} Lorem ipsum "
                                    "dolor sit amet, "
                                    "consectetur adipiscing "
                                    "elit, sed do eiusmod "
                                    "tempor incididunt ut "
                                    "labore et dolore magna "
                                    "aliqua.\n",
                                    "tag": None,
                                    "type": None,
                                }
                            ],
                            "type": "text",
                        }
                    ],
                    "id": None,
                    "tag": "p",
                    "type": "paragraph",
                },
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Lorem ipsum dolor sit "
                                    "amet, consectetur "
                                    "adipiscing elit, sed do "
                                    "eiusmod tempor incididunt "
                                    "ut labore et dolore magna "
                                    "aliqua.\n",
                                    "tag": None,
                                    "type": None,
                                }
                            ],
                            "type": "text",
                        }
                    ],
                    "id": "lorem_ipsum-123",
                    "tag": "p",
                    "type": "paragraph",
                },
            ],
            "filename": "test_id_paragraph_with_invalid_characters_in_id.md",
        }
        assert to_ast(test_file) == expected_markdown

    def test_id_paragraph_with_invalid_characters_in_id_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_id_paragraph_with_invalid_characters_in_id.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<p>{^lorem-ipsum} Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\n' \
            '<p id="lorem_ipsum-123">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html
