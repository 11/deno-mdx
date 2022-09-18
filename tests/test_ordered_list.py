import unittest
from pathlib import Path

from touchdown import markdown, html


TESTCASE_DIR = '../testcases/list/ordered'


class TestOrderedList(unittest.TestCase):
    def test_list_element_numbers_are_corrected_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_list_element_numbers_are_corrected.md')
        assert False

    def test_list_element_numbers_are_corrected_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_list_element_numbers_are_corrected.md')
        assert False

    def test_several_list_elements_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_several_list_elements.md')
        assert False

    def test_several_list_elements_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_several_list_elements.md')
        assert False

    def test_several_lists_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_several_lists.md')
        assert False

    def test_several_lists_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_several_lists.md')
        assert False

    def test_single_list_elemment_markdown(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_list_elemment.md')
        assert False

    def test_single_list_elemment_html(self):
        test_file = Path(f'{TESTCASE_DIR}/test_single_list_elemment.md')
        assert False
