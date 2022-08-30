# Run all tests
#     python -m unittest tests.py
#
# Run all tests and stop at first failure
#     python -m unittest -f tests.py
#     python -m unittest --failfast tests.py
#
# Run all tests, but if ^c is pressed, wait until current test is complete to kill process
#     python -m unittest -c tests.py
#     python -m unittest -catch tests.py


import unittest
from pathlib import Path

import commandline
from .markdown import Markdown as Md


TESTCASE_DIR = '../testcases'


class TestHeader(unittest.TestCase):
    def test_valid_headers(self):
        test_file = f'{TESTCASE_DIR}/test_header.md'
        output = Md(test_file).parse()
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
        assert output == expected_output

    def test_invalid_headers(self):
        pass


class TestText(unittest.TestCase):
    def test_plain_text(self):
        test_file = f'{TESTCASE_DIR}/test_plain_text.md'
        output = Md(test_file).parse()
        expected_output = {
            'filename': header_test.filename,
            'content': [{
                'token': 'paragraph',
                'tag': 'p',
                'content': [{
                    'token': 'text',
                    'content': 'Hello world. This should only result in one paragraph tag and one text token'
                }]
            }]
        }

        assert expected_output == output

    def test_plain_multiline_text(self):
        # test_file = f'{TESTCASE_DIR}/test_plain_text_multiline'
        # output = Md(test_file).parse()
        # expected_output = {

        # }

    def test_formatted_text_1(self):
        test_file = f'{TESTCASE_DIR}/test_formatted_text_1.md'
        output = Md(test_file).parse()
        # expected_output = {
        #     'filename': header_test.filename,
        #     'content': [{
        #         'token': 'paragraph',
        #         'tag': 'p',
        #         'content': [{
        #             'token': 'text',
        #             'content': 'Hello world. This should only result in one paragraph tag and one text token'
        #         }]
        #     }]
        # }

        assert expected_output == output


class TestOrderedList(unittest.TestCase):
    pass


class TestUnorderedList(unittest.TestCase):
    pass


class TestImage(unittest.TestCase):
    pass


class TestTable(unittestTestCase):
    pass

class TestCommandline(Unittest.TestCase):
    def test_files(self):
        # test single file
        args = commandline.parseargs([f'{TESTCASE_DIR}/text/test_plain_text.md'])
        expected_output = [Path(f'{TESTCASE_DIR}/text/test_plain_text.md')]
        assert args['files'] == expected_output

        # test multiple files regex
        args = commandline.parseargs([f'{TESTCASE_DIR}/text/*.md'])
        expected_output = [
            Path(f'{TESTCASE_DIR}/text/test_formatted_text.md'),
            Path(f'{TESTCASE_DIR}/text/test_plain_text.md'),
            Path(f'{TESTCASE_DIR}/text/test_plain_text_multiline.md'),
        ]
        assert args['files'] == expected_output

    def test_flag_output(self):
        # test -o flag shorthand
        args = commandline.parseargs([f'-o=html {TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == 'html'

        # test -o flag shorthand
        output = commandline.parseargs([f'-o=json {TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == 'json'

        # test --output long form flag
        args = commandline.parseargs([f'--output=html {TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == 'html'

        # test --output long form flag
        args = commandline.parseargs([f'--output=json {TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == 'json'

        # test default value is json
        args = commandline.parseargs([f'{TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == json

        # test invalid output type -- expected to fallback to json
        args = commandline.parseargs([f'-o=xml {TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == 'json'

        # test invalid output type -- expected to fallback to json
        args = commandline.parseargs([f'--output=xml {TESTCASE_DIR}/text/test_plain_text.md'])
        assert args['output'] == 'json'




class TestHtml(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

