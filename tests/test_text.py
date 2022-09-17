import unittest
from pprint import pprint
from pathlib import Path

from touchdown import markdown, html


TESTCASE_DIR = './testcases/text'


class TestText(unittest.TestCase):
    maxDiff = None

    # def test_singleline_text(self):
    #     test_file = Path(f'{TESTCASE_DIR}/test_singleline_text.md')
    #     md = markdown(test_file)
    #     expected_output = {
    #         'filename': test_file.name,
    #         'content': [{
    #             'token': 'paragraph',
    #             'tag': 'p',
    #             'content': [{
    #                 'token': 'text',
    #                 'content': 'Hello world. This should only result in one paragraph tag and one text token'
    #             }]
    #         }]
    #     }

    #     assert md == expected_output

    # def test_multiline_text(self):
    #     test_file = Path(f'{TESTCASE_DIR}/test_multiline_text.md')
    #     md = markdown(test_file)
    #     expected_output = {
    #         'filename': test_file.name,
    #         'content': [{
    #             'token': 'paragraph',
    #             'tag': 'p',
    #             'content': [{
    #                 'token': 'text',
    #             }]
    #         }]
    #     }

    #     assert md == expected_output

    # def test_formatted_text_nonoverlap(self):
    #     test_file = Path(f'{TESTCASE_DIR}/test_formatted_text_nonoverlap.md')
    #     md = markdown(test_file)
    #     pprint(md)

    #     expected_output = {
    #         'filename': test_file.name,
    #         'content': [{
    #             'token': 'paragraph',
    #             'tag': 'p',
    #             'content': [{
    #                 'token': 'text',
    #             }]
    #         }]
    #     }

    #     assert md == expected_output


    def test_formatted_text_overlap(self):
        test_file = Path(f'{TESTCASE_DIR}/test_formatted_text_overlap.md')
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
                                {"content": "do ", "tag": None, "type": None},
                                {
                                    "content": "lor",
                                    "tag": ["code"],
                                    "token": ["code"],
                                    "type": "text",
                                },
                                {"content": "sit ", "tag": None, "type": None},
                                {
                                    "content": "amet, consectetur " "adipiscing elit,",
                                    "tag": ["b"],
                                    "token": ["bold"],
                                    "type": "text",
                                },
                                {"content": "sed ", "tag": None, "type": None},
                                {
                                    "content": "do eiusmod tempor "
                                    "incididunt ut labore et "
                                    "dolore magna",
                                    "tag": ["i"],
                                    "token": ["italic"],
                                    "type": "text",
                                },
                                {"content": "aliqua.\n", "tag": None, "type": None},
                            ],
                            "type": "text",
                        }
                    ],
                    "tag": "p",
                    "type": "paragraph",
                }
            ],
            "filename": "test_formatted_text_nonoverlap.md",
        }

        expected_html = '<p><i><s>Lorem </s></i><b><i><s>ips</s></i></b><b><code><i><s>um</s></i></code></b><b><code><s> do lor</s></code></b><code><s> sit</s></code><s> amet</s> consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>'

        print(html(test_file))
        # self.assertEqual(html(test_file), expected_html)
        # self.assertEqual(markdown(test_file), expected_markdown)


    def test_links(self):
        pass
