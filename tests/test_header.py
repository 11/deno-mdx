import unittest
from pathlib import Path

from touchdown import markdown, html


TESTCASE_DIR = '../testcases/header'


class TestHeader(unittest.TestCase):
    def test_header_inside_header_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_header_inside_header.md'
        assert False

    def test_header_inside_header_html(self):
        test_file = f'{TESTCASE_DIR}/test_header_inside_header.md'
        assert False

    def test_invalid_headers_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_invalid_headers.md'
        assert False

    def test_invalid_headers_html(self):
        test_file = f'{TESTCASE_DIR}/test_invalid_headers.md'
        assert False

    def test_valid_headers_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_valid_headers.md'
        expected_markdown = {
            'filename': header_test.filename,
            'content': [{
                'token': 'header',
                'tag': 'h1',
                'content': 'header 1'
            },
            {
                'token': 'header',
                'tag': 'h2',
                'content': 'header 2'
            },
            {
                'token': 'header',
                'tag': 'h3',
                'content': 'header 3'
            },
            {
                'token': 'header',
                'tag': 'h4',
                'content': 'header 4'
            },
            {
                'token': 'header',
                'tag': 'h5',
                'content': 'header 5'
            },
            {
                'token': 'header',
                'tag': 'h6',
                'content': 'header 6'
            }]
        }
        assert markdown(test_file) == expected_markdown

    def test_valid_headers_html(self):
        test_file = f'{TESTCASE_DIR}/test_valid_headers.md'
        assert False
