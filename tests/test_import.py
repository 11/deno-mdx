import unittest
from pathlib import Path
from pprint import pprint

from touchdown import (
    to_html,
    to_ast,
    MarkdownSyntaxError,
)


TESTCASE_DIR = './testcases/import'


class TestImport(unittest.TestCase):
    def test_async_defer_import_creates_error(self):
        """ test that async defer imports are not possible """

        try:
            test_file = Path(f'{TESTCASE_DIR}/test_async_defer_import_creates_error.mdx')
            to_ast(test_file)
        except MarkdownSyntaxError as err:
            assert True
            return

        assert False

    def test_async_import_markdown(self):
        """ test async import works on JS files """

        test_file = Path(f'{TESTCASE_DIR}/test_async_import.mdx')
        expected_markdown = {
            "body": None,
            "filename": "test_async_import.mdx",
            "head": [
                {
                    "async": True,
                    "defer": False,
                    "url": False,
                    "src": "test.js",
                    "tag": "script",
                    "type": "import",
                }
            ],
        }
        assert to_ast(test_file) == expected_markdown

    def test_async_import_html(self):
        """ test async import works on JS files """

        test_file = Path(f'{TESTCASE_DIR}/test_async_import.mdx')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<head>\n' \
            '\t<script type="text/javascript" src="test.js" async></script>\n' \
            '</head>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_async_import_with_css_creates_error(self):
        """ test that async imports fail when loading CSS file """

        try:
            test_file = Path(f'{TESTCASE_DIR}/test_async_import_with_css_creates_error.mdx')
            to_ast(test_file)
        except MarkdownSyntaxError as err:
            assert True
            return

        assert False

    def test_defer_import_markdown(self):
        """ test that defer imports for JS and CSS files work """

        test_file = Path(f'{TESTCASE_DIR}/test_defer_import.mdx')
        expected_markdown = {
            "filename": "test_defer_import.mdx",
            "head": [
                {
                    "type": "import",
                    "tag": "script",
                    "async": False,
                    "defer": True,
                    "url": False,
                    "src": "test.js",
                },
                {
                    "type": "import", 
                    "tag": "link", 
                    "url": False,
                    "href": "test.css", 
                    "rel": "preload"
                },
            ],
            "body": None,
        }
        assert to_ast(test_file) == expected_markdown

    def test_defer_import_html(self):
        """ test that defer imports for JS and CSS files work """

        test_file = Path(f'{TESTCASE_DIR}/test_defer_import.mdx')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<head>\n' \
            '\t<script defer type="text/javascript" src="test.js"></script>\n' \
            '\t<link rel="preload" href="test.css"></link>\n' \
            '</head>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_import_markdown(self):
        """ sanity check that importing JS and CSS files work"""

        test_file = Path(f'{TESTCASE_DIR}/test_import.mdx')
        expected_markdown = {
            "body": None,
            "filename": "test_import.mdx",
            "head": [
                {
                    "async": False,
                    "defer": False,
                    "url": False,
                    "src": "test.js",
                    "tag": "script",
                    "type": "import",
                },
                {
                    "href": "styles/index.css",
                    "url": False,
                    "rel": "stylesheet",
                    "tag": "link",
                    "type": "import",
                },
            ],
        }
        assert to_ast(test_file) == expected_markdown

    def test_import_html(self):
        """ sanity check that importing JS and CSS files work"""

        test_file = Path(f'{TESTCASE_DIR}/test_import.mdx')
        expected_html = \
            '<!DOCTYPE html>\n'\
            '<html>\n'\
            '<head>\n'\
            '\t<script type="text/javascript" src="test.js"></script>\n' \
            '\t<link rel="stylesheet" href="styles/index.css"></link>\n' \
            '</head>\n'\
            '</html>'
        assert to_html(test_file) == expected_html

    def test_import_in_wrong_filetype(self):
        """ test that you can not use import statement in `.md` files"""

        try:
            test_file = Path(f'{TESTCASE_DIR}/test_import_in_wrong_filetype.md')
            to_ast(test_file)
        except MarkdownSyntaxError as err:
            assert True
            return

        assert False

    def test_import_url_markdown(self):
        """ test that importing via URLs works """

        test_file = Path(f'{TESTCASE_DIR}/test_import_url.mdx')
        expected_markdown = {
            "body": None,
            "filename": "test_import_url.mdx",
            "head": [
                {
                    "async": False,
                    "defer": False,
                    "src": "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js",
                    "tag": "script",
                    "type": "import",
                    "url": True,
                }
            ],
        }
        assert to_ast(test_file) == expected_markdown

    def test_import_url_html(self):
        """ test that importing via URLs works """

        test_file = Path(f'{TESTCASE_DIR}/test_import_url.mdx')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<head>\n' \
            '\t<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>\n' \
            '</head>\n' \
            '</html>'
        assert to_html(test_file) == expected_html
