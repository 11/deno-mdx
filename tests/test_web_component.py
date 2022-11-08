import unittest
from pprint import pprint
from pathlib import Path

from touchdown import (
    to_ast,
    to_html,
    MarkdownSyntaxError,
)


TESTCASE_DIR = './testcases/web-component'


class TestWebComponent(unittest.TestCase):
    def test_self_closing_web_component_with_data_attributes_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_self_closing_web_component_with_data_attributes.md'
        expected_markdown = {
            "body": [
                {
                    "content": "<test-element\n"
                    "    data-help='help message'\n"
                    "    data-color='rgba(100,100,100,.8)'\n"
                    "/>",
                    "tag": "test-element",
                    "type": "web_component",
                    "self_closing": True,
                }
            ],
            "filename": "test_self_closing_web_component_with_data_attributes.md",
            "head": None,
        }
        assert to_ast(test_file) == expected_markdown

    def test_self_closing_web_component_with_data_attributes_html(self):
        test_file = f'{TESTCASE_DIR}/test_self_closing_web_component_with_data_attributes.md'
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<test-element\n' \
            "    data-help='help message'\n" \
            "    data-color='rgba(100,100,100,.8)'\n" \
            '></test-element>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_self_closing_web_component_with_functions_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_self_closing_web_component_with_functions.md'
        expected_markdown = {
            "body": [
                {
                    "content": "<test-element\n"
                    "    @click=${(event) => {\n"
                    "        console.log('hello world')\n"
                    "    }}\n"
                    "/>",
                    "self_closing": True,
                    "tag": "test-element",
                    "type": "web_component",
                }
            ],
            "filename": "test_self_closing_web_component_with_functions.md",
            "head": None,
        }
        assert to_ast(test_file) == expected_markdown

    def test_self_closing_web_component_with_functions_html(self):
        test_file = f'{TESTCASE_DIR}/test_self_closing_web_component_with_functions.md'
        expected_html = \
            "<!DOCTYPE html>\n" \
            "<html>\n" \
            "<body>\n" \
            "<test-element\n" \
            "    @click=${(event) => {\n" \
            "        console.log('hello world')\n" \
            "    }}\n" \
            "></test-element>\n" \
            "</body>\n" \
            "</html>"
        assert to_html(test_file) == expected_html

    def test_self_closing_web_component_with_no_attributes_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_self_closing_web_component_with_no_attributes.md'
        expected_markdown = {
            "body": [
                {
                    "content": "<test-element />",
                    "self_closing": True,
                    "tag": "test-element",
                    "type": "web_component",
                },
                {
                    "content": "<test-element/>",
                    "self_closing": True,
                    "tag": "test-element",
                    "type": "web_component",
                },
            ],
            "filename": "test_self_closing_web_component_with_no_attributes.md",
            "head": None,
        }
        assert to_ast(test_file) == expected_markdown

    def test_self_closing_web_component_with_no_attributes_html(self):
        test_file = f'{TESTCASE_DIR}/test_self_closing_web_component_with_no_attributes.md'
        expected_html = \
            "<!DOCTYPE html>\n" \
            "<html>\n" \
            "<body>\n" \
            "<test-element ></test-element>\n" \
            "<test-element></test-element>\n" \
            "</body>\n" \
            "</html>"
        assert to_html(test_file) == expected_html

    def test_web_component_with_children_elements_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_with_children_elements.md'
        expected_markdown = {
            'body': [{
                'self_closing': False,
                'tag': 'test-element',
                'type': 'web_component',
                'content': '<test-element>\n'
                              '    <div>\n'
                              '        <p>Hello world</p>\n'
                              '    </div>\n'
                              '</test-element>\n',
            }],
            'filename': 'test_web_component_with_children_elements.md',
            'head': None
        }
        assert to_ast(test_file) == expected_markdown

    def test_web_component_with_children_elements_html(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_with_children_elements.md'
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<test-element>\n' \
            '    <div>\n' \
            '        <p>Hello world</p>\n' \
            '    </div>\n' \
            '</test-element>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_web_component_with_data_attribute_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_with_data_attribute.md'
        expected_markdown = {
            'body': [{
                'tag': 'test-element',
                'self_closing': False,
                'type': 'web_component',
                'content': '<test-element\n'
                          "  data-message='hello world'\n"
                          "  data-color='rgba(100,100,100,.8)'\n"
                          '></test-element>',
            }],
            'filename': 'test_web_component_with_data_attribute.md',
            'head': None
        }
        assert to_ast(test_file) == expected_markdown

    def test_web_component_with_data_attribute_html(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_with_data_attribute.md'
        expected_html = \
        "<!DOCTYPE html>\n" \
        "<html>\n" \
        "<body>\n" \
        "<test-element\n" \
        "  data-message='hello world'\n" \
        "  data-color='rgba(100,100,100,.8)'\n" \
        "></test-element>\n" \
        "</body>\n" \
        "</html>"
        assert to_html(test_file) == expected_html

    def test_web_component_with_function_attribute_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_with_function_attribute.md'
        expected_markdown = {
            'body': [{
                'content': '<test-element @click=${(event) => {\n'
                          "    console.log('hello world')\n"
                          '}}>\n'
                          '</test-element>',
                'tag': 'test-element',
                'self_closing': False,
                'type': 'web_component'
            }],
            'filename': 'test_web_component_with_function_attribute.md',
            'head': None
        }
        assert to_ast(test_file) == expected_markdown

    def test_web_component_with_function_attribute_html(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_with_function_attribute.md'
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<test-element @click=${(event) => {\n' \
            "    console.log('hello world')\n" \
            '}}>\n' \
            '</test-element>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_web_component_without_attributes_markdown(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_without_attributes.md'
        expected_markdown = {
            'body': [{
                'content': '<test-element></test-element>',
                'tag': 'test-element',
                'type': 'web_component',
                'self_closing': False,
            }],
            'filename': 'test_web_component_without_attributes.md',
            'head': None
        }
        assert to_ast(test_file) == expected_markdown

    def test_web_component_without_attributes_html(self):
        test_file = f'{TESTCASE_DIR}/test_web_component_without_attributes.md'
        expected_html = \
            '<!DOCTYPE html>\n' \
            '<html>\n' \
            '<body>\n' \
            '<test-element></test-element>\n' \
            '</body>\n' \
            '</html>'
        assert to_html(test_file) == expected_html

    def test_web_component_without_closing_tag_markdown(self):
        try:
            test_file = f'{TESTCASE_DIR}/test_web_component_without_closing_tag.md'
            to_ast(test_file)
        except MarkdownSyntaxError as md_err:
            assert True
            return

        assert False


    def test_web_component_without_closing_tag_html(self):
        try:
            test_file = f'{TESTCASE_DIR}/test_web_component_without_closing_tag.md'
            to_html(test_file)
        except MarkdownSyntaxError as md_err:
            assert True
            return

        assert False
