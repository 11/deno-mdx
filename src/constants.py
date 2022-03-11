# TOKENS = {
#     # headers
#     'h1': 'h1',
#     'h2': 'h2',
#     'h3': 'h3',
#     'h4': 'h4',
#     'h5': 'h5',
#     'h6': 'h6',
#
#     # paragraph and styled text
#     'paragraph': 'paragraph',
#     'text': 'text',
#     'code': 'code',
#     'bold': 'bold',
#     'link': 'link',
#     'italic': 'italic',
#     'underline': 'underline',
#     'blockquote': 'blockquote',
#     'strikethrough': 'strikethrough',
#
#     # image
#     'image': 'img',
#
#     # code
#     'codeblock': 'codeblock',
#
#     # lists
#     'list_item': 'list_item',
#     'ordered_list': 'ordered_list',
#     'unordered_list': 'unordered_list',
# }

tokens = {
    'header': r'^(#{1,6}?) (.*?)$',
    'blockquote': r'^\> [\s\S]*$',
    'ordered_list': r'^[0-9]{1,}. ([\s\S]*)$',
    'unordered_list': r'^- ([\s\S]*)$',
    'image': r'^!\[(.*)\]\((.*)\)$',
    'codeblock': {
      'wrap': r'^```$',
      'mid': r'^[\s\S]*$',
    },
}

