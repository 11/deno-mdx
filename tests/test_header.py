import unittest
from pathlib import Path
from pprint import pprint

from touchdown import markdown, html


TESTCASE_DIR = './testcases/header'


class TestHeader(unittest.TestCase):
    def test_header_inside_header_markdown(self):
        """ test that a # characters inside header text does not produce a header """

        test_file = f'{TESTCASE_DIR}/test_header_inside_header.md'
        expected_markdown = {
            "content": [
                {
                    "content": {
                        "content": [
                            {
                                "content": "Lorem ipsum #### subheader " "shouldn't work",
                                "tag": None,
                                "type": None,
                            }
                        ],
                        "type": "text",
                    },
                    "id": "Lorem-ipsum-subheader-shouldnt-work",
                    "tag": "h3",
                    "type": "header",
                }
            ],
            "filename": "test_header_inside_header.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_header_inside_header_html(self):
        """ test that a # characters inside header text does not produce a header """

        test_file = f'{TESTCASE_DIR}/test_header_inside_header.md'
        expected_html = '<h3 id="lorem-ipsum-subheader-shouldnt-work">Lorem ipsum #### subheader shouldn\'t work</h3>'
        assert html(test_file) == expected_html

    def test_header_with_id_markdown(self):
        """ test that a custom ID can be added to a header """

        test_file = Path(f'{TESTCASE_DIR}/test_header_with_id.md')
        expected_markdown = {
            "content": [
                {
                    "content": {
                        "content": [
                            {"content": "Lorem ipsum dolor", "tag": None, "type": None}
                        ],
                        "type": "text",
                    },
                    "id": "lorem-ipsum-dolor",
                    "tag": "h1",
                    "type": "header",
                }
            ],
            "filename": "test_header_with_id.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_header_with_id_html(self):
        """ test that a custom ID can be added to a header """

        test_file = Path(f'{TESTCASE_DIR}/test_header_with_id.md')
        expected_html = '<h1 id="lorem-ipsum-dolor">Lorem ipsum dolor</h1>'
        assert html(test_file) == expected_html

    def test_invalid_headers_markdown(self):
        """ sanity check that 7+ # characters doesn't produce a header"""

        test_file = f'{TESTCASE_DIR}/test_invalid_headers.md'
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "####### This shouldn't be " "a header\n",
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
                                    "content": "########### this doesn't " "make any sense",
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
            ],
            "filename": "test_invalid_headers.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_invalid_headers_html(self):
        """ sanity check that 7+ # characters doesn't produce a header"""

        test_file = f'{TESTCASE_DIR}/test_invalid_headers.md'
        expected_html = \
            '<p>####### This shouldn\'t be a header</p>\n' \
            '<p>########### this doesn\'t make any sense</p>'

        assert html(test_file) == expected_html

    def test_valid_headers_markdown(self):
        """ sanity check that all 6 header types are correctly parsed """

        test_file = f'{TESTCASE_DIR}/test_valid_headers.md'
        expected_markdown ={
            "content": [
                {
                    "content": {
                        "content": [{"content": "header 1", "tag": None, "type": None}],
                        "type": "text",
                    },
                    'id': 'header-1',
                    "tag": "h1",
                    "type": "header",

                },
                {
                    "content": {
                        "content": [{"content": "header 2", "tag": None, "type": None}],
                        "type": "text",
                    },
                    'id': 'header-2',
                    "tag": "h2",
                    "type": "header",
                },
                {
                    "content": {
                        "content": [{"content": "header 3", "tag": None, "type": None}],
                        "type": "text",
                    },
                    'id': 'header-3',
                    "tag": "h3",
                    "type": "header",
                },
                {
                    "content": {
                        "content": [{"content": "header 4", "tag": None, "type": None}],
                        "type": "text",
                    },
                    'id': 'header-4',
                    "tag": "h4",
                    "type": "header",
                },
                {
                    "content": {
                        "content": [{"content": "header 5", "tag": None, "type": None}],
                        "type": "text",
                    },
                    'id': 'header-5',
                    "tag": "h5",
                    "type": "header",
                },
                {
                    "content": {
                        "content": [{"content": "header 6", "tag": None, "type": None}],
                        "type": "text",
                    },
                    'id': 'header-6',
                    "tag": "h6",
                    "type": "header",
                },
            ],
            "filename": "test_valid_headers.md",
        }
 
        assert markdown(test_file) == expected_markdown

    def test_valid_headers_html(self):
        """ sanity check that all 6 header types are correctly parsed """

        test_file = f'{TESTCASE_DIR}/test_valid_headers.md'
        expected_html = \
            '<h1 id="header-1">header 1</h1>\n' \
            '<h2 id="header-2">header 2</h2>\n' \
            '<h3 id="header-3">header 3</h3>\n' \
            '<h4 id="header-4">header 4</h4>\n' \
            '<h5 id="header-5">header 5</h5>\n' \
            '<h6 id="header-6">header 6</h6>'

        assert html(test_file) == expected_html
