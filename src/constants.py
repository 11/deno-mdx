tokens = {
    'header': r'^(#{1,6}?) (.*?)$',
    'blockquote': r'^\> [\s\S]*$',
    'ordered_list': r'^[0-9]{1,}. ([\s\S]*)$',
    'unordered_list': r'^- ([\s\S]*)$',
    'image': r'^!\[(.*)\]\((.*)\)$',
    'codeblock': r'^```$',
}

