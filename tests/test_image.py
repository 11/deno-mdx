import unittest
from pathlib import Path
from pprint import pprint

from touchdown import to_html, to_ast 


TESTCASE_DIR = './testcases/image'


class TestImage(unittest.TestCase):
    def test_image_with_default_uri_markdown(self):
        """ test user can manually palce `#` sign in URI """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_default_uri.md')
        expected_markdown = {
            "head": None,
            "body": [{"alt": "alt text", "tag": "img", "type": "image", "uri": "#"}],
            "filename": "test_image_with_default_uri.md",
        }

        assert to_ast(test_file) == expected_markdown

    def test_image_with_default_uri_html(self):
        """ test user can manually palce `#` sign in URI """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_default_uri.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<img alt="alt text" src="#" />\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_image_with_link_in_uri_markdown(self):
        """ test images can include link in URI """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_link_in_uri.md')
        expected_markdown = {
            'head': None,
            'body': [{
                'alt': 'alt text',
                'tag': 'img',
                'type': 'image',
                'uri': 'https://media.newyorker.com/photos/5a95a5b13d9089123c9fdb7e/1:1/w_3289,h_3289,c_limit/Petrusich-Dont-Mess-with-the-Birds.jpg'
            }],
            'filename': 'test_image_with_link_in_uri.md'
         }
        assert to_ast(test_file) == expected_markdown

    def test_image_with_link_in_uri_html(self):
        """ test images can include link in URI """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_link_in_uri.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<img alt="alt text" src="https://media.newyorker.com/photos/5a95a5b13d9089123c9fdb7e/1:1/w_3289,h_3289,c_limit/Petrusich-Dont-Mess-with-the-Birds.jpg" />\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_image_with_local_file_uri_markdown(self):
        """ sanity check that markdown will find local images """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_local_file_uri.md')
        expected_markdown = {
            "head": None,
            "body": [
                {
                    "alt": "eagle",
                    "tag": "img",
                    "type": "image",
                    "uri": "/testcases/image/eagle.png",
                }
            ],
            "filename": "test_image_with_local_file_uri.md",
        }
        assert to_ast(test_file) == expected_markdown

    def test_image_with_local_file_uri_html(self):
        """ sanity check that markdown will find local images """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_local_file_uri.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<img alt="eagle" src="/testcases/image/eagle.png" />\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_image_with_local_no_uri_markdown(self):
        """ test that defulat URI is `#` """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_no_uri.md')
        expected_markdown = {
            "head": None,
            "body": [{"alt": "alt text", "tag": "img", "type": "image", "uri": ""}],
            "filename": "test_image_with_no_uri.md",
        }
        assert to_ast(test_file) == expected_markdown

    def test_image_with_local_no_uri_html(self):
        """ test that defulat URI is `#` """

        test_file = Path(f'{TESTCASE_DIR}/test_image_with_no_uri.md')
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<img alt="alt text" src="#" />\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html
