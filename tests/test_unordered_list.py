import unittest
from pprint import pprint
from pathlib import Path

from touchdown import to_ast, to_html


TESTCASE_DIR = './testcases/list/unordered'


class TestUnorderedList(unittest.TestCase):
    def test_several_list_elements_markdown(self):
        """ tests that a single list will append multiple list elements """

        test_file = Path(f'{TESTCASE_DIR}/test_several_list_elements.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "Lorem ipsum " "dolor sit amet",
                                        "tag": None,
                                        "type": None,
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
                                    {
                                        "content": "consectetur " "adipiscing " "elit",
                                        "tag": None,
                                        "type": None,
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
                                    {
                                        "content": "sed do eiusmod " "tempor " "incididunt ",
                                        "tag": None,
                                        "type": None,
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
                                    {
                                        "content": "ut labore et " "dolore magna " "aliqua.",
                                        "tag": None,
                                        "type": None,
                                    }
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
            "filename": "test_several_list_elements.md",
        }

        assert to_ast(test_file) == expected_markdown

    def test_several_list_elements_html(self):
        """ tests that a single list will append multiple list elements """

        test_file = Path(f'{TESTCASE_DIR}/test_several_list_elements.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ul>\n' \
            '\t<li>Lorem ipsum dolor sit amet</li>\n' \
            '\t<li>consectetur adipiscing elit</li>\n' \
            '\t<li>sed do eiusmod tempor incididunt </li>\n' \
            '\t<li>ut labore et dolore magna aliqua.</li>\n' \
            '</ul>\n' \
            '</body>\n' \
            '</html>'

        assert to_html(test_file) == expected_html

    def test_several_lists_markdown(self):
        """ tests if newline starts a new list """

        test_file = Path(f'{TESTCASE_DIR}/test_several_lists.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "Lorem ipsum " "dolor sit amet",
                                        "tag": None,
                                        "type": None,
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
                                    {
                                        "content": "consectetur "
                                        "adipiscing "
                                        "elit sed do "
                                        "eiusmod tempor "
                                        "incididunt ut "
                                        "labore et "
                                        "dolore magna "
                                        "aliqua",
                                        "tag": None,
                                        "type": None,
                                    }
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                    ],
                    "tag": "ul",
                    "type": "unordered_list",
                },
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "Ut enim ad " "minim veniam",
                                        "tag": None,
                                        "type": None,
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
                                    {"content": "quis nostrud ", "tag": None, "type": None}
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                        {
                            "content": {
                                "content": [
                                    {"content": "exercitation ", "tag": None, "type": None}
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        },
                    ],
                    "tag": "ul",
                    "type": "unordered_list",
                },
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "ullamco "
                                        "laboris nisi "
                                        "ut aliquip ex "
                                        "ea commodo "
                                        "consequat",
                                        "tag": None,
                                        "type": None,
                                    }
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        }
                    ],
                    "tag": "ul",
                    "type": "unordered_list",
                },
            ],
            "filename": "test_several_lists.md",
        }
        assert to_ast(test_file) == expected_markdown

    def test_several_lists_html(self):
        """ tests if newline starts a new list """

        test_file = Path(f'{TESTCASE_DIR}/test_several_lists.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ul>\n' \
            '\t<li>Lorem ipsum dolor sit amet</li>\n' \
            '\t<li>consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</li>\n' \
            '</ul>\n' \
            '<ul>\n' \
            '\t<li>Ut enim ad minim veniam</li>\n' \
            '\t<li>quis nostrud </li>\n' \
            '\t<li>exercitation </li>\n' \
            '</ul>\n' \
            '<ul>\n' \
            '\t<li>ullamco laboris nisi ut aliquip ex ea commodo consequat</li>\n' \
            '</ul>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_single_list_element_markdown(self):
        """ sanity test that validates if a single list element is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_single_list_element.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "content": [
                        {
                            "content": {
                                "content": [
                                    {"content": "this is a test", "tag": None, "type": None}
                                ],
                                "type": "text",
                            },
                            "tag": "li",
                            "type": "listitem",
                        }
                    ],
                    "tag": "ul",
                    "type": "unordered_list",
                }
            ],
            "filename": "test_single_list_element.md",
        }
        assert to_ast(test_file) == expected_markdown

    def test_single_list_element_html(self):
        """ sanity test that validates if a single list element is correctly parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_single_list_element.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ul>\n' \
            '\t<li>this is a test</li>\n' \
            '</ul>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html
