import unittest
from pathlib import Path
from pprint import pprint

from touchdown import html, markdown


TESTCASE_DIR = './testcases/link'


class TestLink(unittest.TestCase):
    def test_link_around_image_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_link_around_image.md')
        assert False

    def test_link_around_image_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_link_around_image.md')
        assert False

    def test_link_in_blockquote_markdown(self):
        """ testing links are parsed out correctly inside blockquote """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_blockquote.md')
        expected_markdown = {
            "content": [
                {
                    "content": {
                        "content": [
                            {
                                "content": "Lorem ipsum dolor sit amet, " "consectetur ",
                                "tag": None,
                                "type": None,
                            },
                            {
                                "content": "adipiscing elit",
                                "href": "https://google.com",
                                "tag": ["a"],
                                "type": "link",
                            },
                            {
                                "content": ", sed do eiusmod tempor "
                                "incididunt ut labore et "
                                "dolore magna aliqua. Ut "
                                "enim ad minim veniam, quis "
                                "nostrud exercitation "
                                "ullamco laboris nisi ut "
                                "aliquip ex ea commodo "
                                "consequat",
                                "tag": None,
                                "type": None,
                            },
                        ],
                        "type": "text",
                    },
                    "tag": "blockquote",
                    "type": "blockquote",
                }
            ],
            "filename": "test_link_in_blockquote.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_link_in_blockquote_html(self):
        """ testing links are parsed out correctly inside blockquote """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_blockquote.md')
        expected_html = '<blockquote>Lorem ipsum dolor sit amet, consectetur <a href="https://google.com">adipiscing elit</a>, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat</blockquote>'
        assert html(test_file) == expected_html

    def test_link_in_decorated_text_markdown(self):
        """ test that styling is still correctly applied to links after parsing text decoration """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_decorated_text.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {"content": "Lorem ipsum ", "tag": None, "type": None},
                                {
                                    "content": "dolor sit ",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {
                                    "content": "amet, ",
                                    "tag": ["b", "s"],
                                    "token": ["bold", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": "consectetur",
                                    "href": "https://google.com",
                                    "tag": ["a", "b", "s"],
                                    "type": "link",
                                },
                                {
                                    "content": " adipiscing",
                                    "tag": ["b", "s"],
                                    "token": ["bold", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": "elit",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {
                                    "content": ", sed do eiusmod tempor "
                                    "incididunt ut labore et "
                                    "dolore magna aliqua. Ut "
                                    "enim ad minim veniam, quis "
                                    "nostrud exercitation "
                                    "ullamco laboris nisi ut "
                                    "aliquip ex ea commodo "
                                    "consequat",
                                    "tag": None,
                                    "type": None,
                                },
                            ],
                            "type": "text",
                        }
                    ],
                    'id': None,
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_link_in_decorated_text.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_link_in_decorated_text_html(self):
        """ test that styling is still correctly applied to links after parsing text decoration """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_decorated_text.md')
        expected_html = '<p>Lorem ipsum <b>dolor sit </b><b><s>amet, </s></b><b><s><a href="https://google.com">consectetur</a></s></b><b><s> adipiscing</s></b><b>elit</b>, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat</p>'
        assert html(test_file) == expected_html

    def test_link_in_header_markdown(self):
        """ test links are correctly applied inside headers """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_header.md')
        expected_markdown = {
            "content": [
                {
                    "content": {
                        "content": [
                            {
                                "content": "google",
                                "href": "https://google.com",
                                "tag": ["a"],
                                "type": "link",
                            }
                        ],
                        "type": "text",
                    },
                    "id": "google",
                    "tag": "h1",
                    "type": "header",
                },
                {
                    "content": {
                        "content": [
                            {"content": "Lorem ipsum ", "tag": None, "type": None},
                            {
                                "content": "dolor",
                                "href": "https://google.com",
                                "tag": ["a"],
                                "type": "link",
                            },
                            {"content": " sit amet", "tag": None, "type": None},
                        ],
                        "type": "text",
                    },
                    "id": "lorem-ipsum-dolor-sit-amet",
                    "tag": "h3",
                    "type": "header",
                },
                {
                    "content": {
                        "content": [
                            {"content": "Lorem ", "tag": None, "type": None},
                            {
                                "content": "ipsum ",
                                "tag": ["b"],
                                "token": ["bold"],
                                "type": "text",
                            },
                            {
                                "content": "dolor",
                                "href": "https://google.com",
                                "tag": ["a", "b"],
                                "type": "link",
                            },
                            {
                                "content": " sit",
                                "tag": ["b"],
                                "token": ["bold"],
                                "type": "text",
                            },
                            {"content": " amet", "tag": None, "type": None},
                        ],
                        "type": "text",
                    },
                    "id": "lorem-ipsum-dolor-sit-amet",
                    "tag": "h4",
                    "type": "header",
                },
            ],
            "filename": "test_link_in_header.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_link_in_header_html(self):
        """ test links are correctly applied inside headers """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_header.md')
        expected_html = \
            '<h1 id="google"><a href="https://google.com">google</a></h1>\n' \
            '<h3 id="lorem-ipsum-dolor-sit-amet">Lorem ipsum <a href="https://google.com">dolor</a> sit amet</h3>\n' \
            '<h4 id="lorem-ipsum-dolor-sit-amet">Lorem <b>ipsum </b><b><a href="https://google.com">dolor</a></b><b> sit</b> amet</h4>'
        assert html(test_file) == expected_html

    def test_link_in_ordered_list_markdown(self):
        """ test text inside ordered lists is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_ordered_list.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "google",
                                        "href": "https://google.com",
                                        "tag": ["a"],
                                        "type": "link",
                                    },
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                        {
                            "content": {
                                "content": [
                                    {"content": "Lorem ipsum ", "tag": None, "type": None},
                                    {
                                        "content": "dolor",
                                        "href": "https://google.com",
                                        "tag": ["a"],
                                        "type": "link",
                                    },
                                    {"content": " sit amet", "tag": None, "type": None},
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                        {
                            "content": {
                                "content": [
                                    {"content": "Lorem ", "tag": None, "type": None},
                                    {
                                        "content": "ipsum ",
                                        "tag": ["b"],
                                        "token": ["bold"],
                                        "type": "text",
                                    },
                                    {
                                        "content": "dolor",
                                        "href": "https://google.com",
                                        "tag": ["a", "b"],
                                        "type": "link",
                                    },
                                    {
                                        "content": " sit",
                                        "tag": ["b"],
                                        "token": ["bold"],
                                        "type": "text",
                                    },
                                    {"content": " amet", "tag": None, "type": None},
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                    ],
                    "tag": "ol",
                    "type": "ordered_list",
                }
            ],
            "filename": "test_link_in_ordered_list.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_link_in_ordered_list_html(self):
        """ test text inside ordered lists is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_ordered_list.md')
        expected_html = \
            '<ol>\n' \
            '\t<li><a href="https://google.com">google</a></li>\n' \
            '\t<li>Lorem ipsum <a href="https://google.com">dolor</a> sit amet</li>\n' \
            '\t<li>Lorem <b>ipsum </b><b><a href="https://google.com">dolor</a></b><b> sit</b> amet</li>\n' \
            '</ol>'

        assert html(test_file) == expected_html

    def test_link_in_plain_text_markdown(self):
        """ sanity check that tests in plain text work """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_plain_text.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Lorem ipsum dolor sit amet",
                                    "href": "https://google.com",
                                    "tag": ["a"],
                                    "type": "link",
                                },
                                {
                                    "content": ", consectetur adipiscing "
                                    "elit, sed do eiusmod "
                                    "tempor incididunt ut "
                                    "labore et dolore magna "
                                    "aliqua. ",
                                    "tag": None,
                                    "type": None,
                                },
                                {
                                    "content": "Ut enim ad minim veniam",
                                    "href": "https://google.com",
                                    "tag": ["a"],
                                    "type": "link",
                                },
                                {
                                    "content": ", quis nostrud "
                                    "exercitation ullamco "
                                    "laboris nisi ut aliquip ex "
                                    "ea commodo consequat",
                                    "tag": None,
                                    "type": None,
                                },
                            ],
                            "type": "text",
                        }
                    ],
                    "id": None,
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_link_in_plain_text.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_link_in_plain_text_html(self):
        """ sanity check that tests in plain text work """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_plain_text.md')
        expected_html = '<p><a href="https://google.com">Lorem ipsum dolor sit amet</a>, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. <a href="https://google.com">Ut enim ad minim veniam</a>, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat</p>'
        assert html(test_file) == expected_html

    def test_link_in_unordered_list_markdown(self):
        """ test text inside unordered lists is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_unordered_list.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "google",
                                        "href": "https://google.com",
                                        "tag": ["a"],
                                        "type": "link",
                                    }
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                        {
                            "content": {
                                "content": [
                                    {"content": "Lorem ipsum ", "tag": None, "type": None},
                                    {
                                        "content": "dolor",
                                        "href": "https://google.com",
                                        "tag": ["a"],
                                        "type": "link",
                                    },
                                    {"content": " sit amet", "tag": None, "type": None},
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                        {
                            "content": {
                                "content": [
                                    {"content": "Lorem ", "tag": None, "type": None},
                                    {
                                        "content": "ipsum ",
                                        "tag": ["b"],
                                        "token": ["bold"],
                                        "type": "text",
                                    },
                                    {
                                        "content": "dolor",
                                        "href": "https://google.com",
                                        "tag": ["a", "b"],
                                        "type": "link",
                                    },
                                    {
                                        "content": " sit",
                                        "tag": ["b"],
                                        "token": ["bold"],
                                        "type": "text",
                                    },
                                    {"content": " amet", "tag": None, "type": None},
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                    ],
                    "tag": "ul",
                    "type": "unordered_list",
                }
            ],
            "filename": "test_link_in_unordered_list.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_link_in_unordered_list_html(self):
        """ test text inside unordered lists is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_link_in_unordered_list.md')
        expected_html = \
            '<ul>\n' \
            '\t<li><a href="https://google.com">google</a></li>\n' \
            '\t<li>Lorem ipsum <a href="https://google.com">dolor</a> sit amet</li>\n' \
            '\t<li>Lorem <b>ipsum </b><b><a href="https://google.com">dolor</a></b><b> sit</b> amet</li>\n' \
            '</ul>'

        assert html(test_file) == expected_html
