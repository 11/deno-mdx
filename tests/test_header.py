import unittest
from pathlib import Path


TESTCASE_DIR = '../testcases'


class TestHeader(unittest.TestCase):
    def test_valid_headers(self):
        test_file = f'{TESTCASE_DIR}/test_header.md'
        tokens = Md(test_file).markdown
        expected_output = {
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
        assert tokens == expected_output

    def test_invalid_headers(self):
        test_file = f'{TESTCASE_DIR}/test_invalid_headers.md'
        tokens = Md(test_file).markdown

        assert tokens == False
