import unittest
from pathlib import Path

from touchdown import to_ast, to_html


TESTCASE_DIR = './testcases/list/ordered'


class TestOrderedList(unittest.TestCase):
    def test_list_element_numbers_are_corrected_markdown(self):
        """ test that the list element number is normalized """

        test_file = Path(f'{TESTCASE_DIR}/test_list_element_numbers_are_corrected.md')
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
                        {
                            "content": {
                                "content": [
                                    {
                                        "content": "the list "
                                        "elmeents "
                                        "should be "
                                        "corrected to "
                                        "be 1,2,3,4,5",
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
                    "tag": "ol",
                    "type": "ordered_list",
                }
            ],
            "filename": "test_list_element_numbers_are_corrected.md",
        }

        assert to_ast(test_file) == expected_markdown

    def test_list_element_numbers_are_corrected_html(self):
        """ test that the list element number is normalized """

        test_file = Path(f'{TESTCASE_DIR}/test_list_element_numbers_are_corrected.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ol>\n' \
            '\t<li>Lorem ipsum dolor sit amet</li>\n' \
            '\t<li>consectetur adipiscing elit</li>\n' \
            '\t<li>sed do eiusmod tempor incididunt </li>\n' \
            '\t<li>ut labore et dolore magna aliqua.</li>\n' \
            '\t<li>the list elmeents should be corrected to be 1,2,3,4,5</li>\n' \
            '</ol>\n' \
            '</body>\n' \
            '</html>'
 
        assert to_html(test_file) == expected_html

    def test_several_list_elements_markdown(self):
        """ test that a single orderd list will append multiple list elements """

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
                    "tag": "ol",
                    "type": "ordered_list",
                }
            ],
            "filename": "test_several_list_elements.md",
        }
 
        assert to_ast(test_file) == expected_markdown

    def test_several_list_elements_html(self):
        """ test that a single orderd list will append multiple list elements """

        test_file = Path(f'{TESTCASE_DIR}/test_several_list_elements.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ol>\n' \
            '\t<li>Lorem ipsum dolor sit amet</li>\n' \
            '\t<li>consectetur adipiscing elit</li>\n' \
            '\t<li>sed do eiusmod tempor incididunt </li>\n' \
            '\t<li>ut labore et dolore magna aliqua.</li>\n' \
            '</ol>\n' \
            '</body>\n' \
            '</html>'
 
        assert to_html(test_file) == expected_html

    def test_several_lists_markdown(self):
        """ test that list elements are correctly appended to their respective list """

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
                    "tag": "ol",
                    "type": "ordered_list",
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
                    "tag": "ol",
                    "type": "ordered_list",
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
                    "tag": "ol",
                    "type": "ordered_list",
                },
            ],
            "filename": "test_several_lists.md",
        }

        assert to_ast(test_file) == expected_markdown

    def test_several_lists_html(self):
        """ test that list elements are correctly appended to their respective list """

        test_file = Path(f'{TESTCASE_DIR}/test_several_lists.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ol>\n' \
            '\t<li>Lorem ipsum dolor sit amet</li>\n' \
            '\t<li>consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</li>\n' \
            '</ol>\n' \
            '<ol>\n' \
            '\t<li>Ut enim ad minim veniam</li>\n' \
            '\t<li>quis nostrud </li>\n' \
            '\t<li>exercitation </li>\n' \
            '</ol>\n' \
            '<ol>\n' \
            '\t<li>ullamco laboris nisi ut aliquip ex ea commodo consequat</li>\n' \
            '</ol>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_single_list_element_markdown(self):
        """ sanity test for creating a ordered list with 1 list element """

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
                    "tag": "ol",
                    "type": "ordered_list",
                }
            ],
            "filename": "test_single_list_element.md",
        }

        assert to_ast(test_file) == expected_markdown

    def test_single_list_element_html(self):
        """ sanity test for creating a ordered list with 1 list element """

        test_file = Path(f'{TESTCASE_DIR}/test_single_list_element.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<ol>\n' \
            '\t<li>this is a test</li>\n' \
            '</ol>\n' \
            '</body>\n' \
            '</html>'

        assert to_html(test_file) == expected_html
