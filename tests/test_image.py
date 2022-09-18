import unittest
from pathlib import Path


TESTCASE_DIR = '../testcases/image'


class TestImage(unittest.TestCase):
    def test_image_with_default_uri_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_default_uri.md')
        assert False

    def test_image_with_default_uri_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_default_uri.md')
        assert False

    def test_image_with_link_in_uri_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_link_in_uri.md')
        assert False

    def test_image_with_link_in_uri_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_link_in_uri.md')
        assert False

    def test_image_with_local_file_uri_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_local_file_uri.md')
        assert False

    def test_image_with_local_file_uri_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_local_file_uri.md')
        assert False

    def test_image_with_local_no_uri_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_no_uri.md')
        assert False

    def test_image_with_local_no_uri_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_image_with_no_uri.md')
        assert False
