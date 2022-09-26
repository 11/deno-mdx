import unittest
from pprint import pprint
from pathlib import Path

from touchdown import markdown, html


TESTCASE_DIR = './testcases/text'


class TestText(unittest.TestCase):
    def test_formatted_text_nonoverlap_markdown(self):
        """ testign text with non-overlapping tags """

        test_file = Path(f'{TESTCASE_DIR}/test_formatted_text_nonoverlap.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Lorem ipsum",
                                    "tag": ["s"],
                                    "token": ["strikethrough"],
                                    "type": "text",
                                },
                                {"content": " do ", "tag": None, "type": None},
                                {
                                    "content": "lor",
                                    "tag": ["code"],
                                    "token": ["code"],
                                    "type": "text",
                                },
                                {"content": " sit ", "tag": None, "type": None},
                                {
                                    "content": "amet, consectetur " "adipiscing elit,",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {"content": " sed ", "tag": None, "type": None},
                                {
                                    "content": "do eiusmod tempor "
                                    "incididunt ut labore et "
                                    "dolore magna",
                                    "tag": ["i"],
                                    "token": ["italic"],
                                    "type": "text",
                                },
                                {"content": " aliqua.\n", "tag": None, "type": None},
                            ],
                            "type": "text",
                        }
                    ],
                    "id": None,
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_formatted_text_nonoverlap.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_formatted_text_nonoverlap_html(self):
        """ testing text with non-overlapping tags """

        test_file = Path(f'{TESTCASE_DIR}/test_formatted_text_nonoverlap.md')
        expected_html = '<p><s>Lorem ipsum</s> do <code>lor</code> sit <b>amet, consectetur adipiscing elit,</b> sed <i>do eiusmod tempor incididunt ut labore et dolore magna</i> aliqua.</p>'
        assert html(test_file) == expected_html

    def test_formatted_text_overlap_markdown(self):
        """ testing formatted text with overlaping tags"""

        test_file = Path(f'{TESTCASE_DIR}/test_formatted_text_overlap.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Lorem ",
                                    "tag": ["i", "s"],
                                    "token": ["italic", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": "ips",
                                    "tag": ["b", "i", "s"],
                                    "token": ["bold", "italic", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": "um",
                                    "tag": ["b", "i", "code", "s"],
                                    "token": ["bold", "italic", "code", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": " do lor",
                                    "tag": ["b", "code", "s"],
                                    "token": ["bold", "code", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": " sit",
                                    "tag": ["code", "s"],
                                    "token": ["code", "strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": " amet",
                                    "tag": ["s"],
                                    "token": ["strikethrough"],
                                    "type": "text",
                                },
                                {
                                    "content": ", consectetur adipiscing "
                                    "elit, sed do eiusmod "
                                    "tempor incididunt ut "
                                    "labore et dolore magna "
                                    "aliqua.\n",
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
            "filename": "test_formatted_text_overlap.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_formatted_text_overlap_html(self):
        """ testing formatted text with overlaping tags"""

        expected_html = '<p><i><s>Lorem </s></i><b><i><s>ips</s></i></b><b><code><i><s>um</s></i></code></b><b><code><s> do lor</s></code></b><code><s> sit</s></code><s> amet</s>, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>'
        test_file = Path(f'{TESTCASE_DIR}/test_formatted_text_overlap.md')
        assert html(test_file) == expected_html

    def test_multiline_text_markdown(self):
        """ tests that multiple lines of plane text are converted to several paragraph tags """

        test_file = Path(f'{TESTCASE_DIR}/test_multiline_text.md')
        expected_markdown = {
            "content": [
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
                    'id': None,
                    "tag": "p",
                    "type": "paragraph",
                },
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Ut enim ad minim veniam, "
                                    "quis nostrud exercitation "
                                    "ullamco laboris nisi ut "
                                    "aliquip ex ea commodo "
                                    "consequat.\n",
                                    "tag": None,
                                    "type": None,
                                }
                            ],
                            "type": "text",
                        }
                    ],
                    'id': None,
                    "tag": "p",
                    "type": "paragraph",
                },
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Duis aute irure dolor in "
                                    "reprehenderit in voluptate "
                                    "velit esse cillum dolore "
                                    "eu fugiat nulla pariatur. "
                                    "Excepteur sint occaecat "
                                    "cupidatat non proident, "
                                    "sunt in culpa qui officia "
                                    "deserunt mollit anim id "
                                    "est laborum.\n",
                                    "tag": None,
                                    "type": None,
                                }
                            ],
                            "type": "text",
                        }
                    ],
                    'id': None,
                    "tag": "p",
                    "type": "paragraph",
                },
            ],
            "filename": "test_multiline_text.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_multiline_text_html(self):
        """ tests that multiple lines of plane text are converted to several paragraph tags """

        test_file = Path(f'{TESTCASE_DIR}/test_multiline_text.md')
        expected_html = '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\n<p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>\n<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>'
        assert html(test_file) == expected_html

    def test_mutliple_inline_mathblocks_markdown(self):
        """ test that multiple inline mathblocks parsing takes care of off by 1's and decorative text still works """

        test_file = Path(f'{TESTCASE_DIR}/test_multiple_inline_mathblocks.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {"content": "If ", "tag": None, "type": None},
                                {
                                    "content": "$\\hat{\\mathcal{E}}_D(x) "
                                    "\\leq \\varepsilon$",
                                    "tag": ["span"],
                                    "type": "math",
                                },
                                {
                                    "content": ", we say the model is ",
                                    "tag": None,
                                    "type": None,
                                },
                                {"content": "$\\varepsilon$", "tag": ["span"], "type": "math"},
                                {"content": "-", "tag": None, "type": None},
                                {
                                    "content": "confident",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {
                                    "content": " in its prediction at ",
                                    "tag": None,
                                    "type": None,
                                },
                                {"content": "$x$", "tag": ["span"], "type": "math"},
                                {
                                    "content": "; otherwise, the model is ",
                                    "tag": None,
                                    "type": None,
                                },
                                {"content": "$\\varepsilon$", "tag": ["span"], "type": "math"},
                                {"content": "-", "tag": None, "type": None},
                                {
                                    "content": "uncertain",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {"content": ". The ", "tag": None, "type": None},
                                {"content": "$\\varepsilon$", "tag": ["span"], "type": "math"},
                                {"content": "-", "tag": None, "type": None},
                                {
                                    "content": "confidence region",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {
                                    "content": " is defined as the set of "
                                    "all points where we are "
                                    "confident, denoted ",
                                    "tag": None,
                                    "type": None,
                                },
                                {
                                    "content": "$\\hat{C}_\\varepsilon = "
                                    "\\{ x \\in X \\mid "
                                    "\\hat{\\mathcal{E}}_D(x) "
                                    "\\leq \\varepsilon \\} "
                                    "\\subseteq X$",
                                    "tag": ["span"],
                                    "type": "math",
                                },
                                {"content": ".", "tag": None, "type": None},
                            ],
                            "type": "text",
                        }
                    ],
                    "id": None,
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_multiple_inline_mathblocks.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_mutliple_inline_mathblocks_html(self):
        """ test that multiple inline mathblocks parsing takes care of off by 1's and decorative text still works """

        test_file = Path(f'{TESTCASE_DIR}/test_multiple_inline_mathblocks.md')
        expected_html = '<p>If <span>$\\hat{\\mathcal{E}}_D(x) \\leq \\varepsilon$</span>, we say the model is <span>$\\varepsilon$</span>-<b>confident</b> in its prediction at <span>$x$</span>; otherwise, the model is <span>$\\varepsilon$</span>-<b>uncertain</b>. The <span>$\\varepsilon$</span>-<b>confidence region</b> is defined as the set of all points where we are confident, denoted <span>$\\hat{C}_\\varepsilon = \\{ x \\in X \\mid \\hat{\\mathcal{E}}_D(x) \\leq \\varepsilon \\} \\subseteq X$</span>.</p>'
        assert html(test_file) == expected_html


    def test_single_inline_mathblock_markdown(self):
        """ santiy check that a single inline mathblock can be parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_single_inline_mathblock.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {"content": "this is some math: ", "tag": None, "type": None},
                                {
                                    "content": "$\\mathcal{E}(y,y') = 0 " "\\iff y = y'$",
                                    "tag": ["span"],
                                    "type": "math",
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
            "filename": "test_single_inline_mathblock.md",
        }
        assert markdown(test_file) == expected_markdown

    def test_single_inline_mathblock_html(self):
        """ santiy check that a single inline math block can be parsed """

        test_file = Path(f'{TESTCASE_DIR}/test_single_inline_mathblock.md')
        expected_html = '<p>this is some math: <span>$\\mathcal{E}(y,y\') = 0 \\iff y = y\'$</span></p>'
        assert html(test_file) == expected_html

    def test_singleline_text_markdown(self):
        """ sanity check that single of text is interpreted as a paragraph tag """

        test_file = Path(f'{TESTCASE_DIR}/test_singleline_text.md')
        expected_markdown = {
            "content": [
                {
                    "content": [
                        {
                            "content": [
                                {
                                    "content": "Hello world. This should "
                                    "only result in one "
                                    "paragraph tag and one text "
                                    "token\n",
                                    "tag": None,
                                    "type": None,
                                }
                            ],
                            "type": "text",
                        }
                    ],
                    'id': None,
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_singleline_text.md",
        }

        assert markdown(test_file) == expected_markdown

    def test_singleline_text_html(self):
        """ sanity check that single of text is interpreted as a paragraph tag """

        test_file = Path(f'{TESTCASE_DIR}/test_singleline_text.md')
        expected_html = '<p>Hello world. This should only result in one paragraph tag and one text token</p>'
        assert html(test_file) == expected_html
