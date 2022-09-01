MARKDOWN_REGEXS = {
    # https://www.debuggex.com/r/yJLwFDiFjDuifTSr
    'header': r'^(#{1,6}?) (.*?)$',

    # https://www.debuggex.com/r/4xeF1p18gQjjhAe9
    'blockquote': r'^\> [\s\S]*$',

    # https://www.debuggex.com/r/s2BZUI9PedP0m5O-
    'ordered_list': r'^\s*[0-9]{1,}. ([\s\S]*)\n$',

    # https://www.debuggex.com/r/9hQERKefFNj_3CsR
    'unordered_list': r'^\s*- ([\s\S]*)\n$',

    # https://www.debuggex.com/r/u64sYbgHehYd5zet
    'image': r'^!\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/dnmmbV9HXMOBFQPa
    'link': r'^\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/7D4R7b9LVt8QbJ1l
    'codeblock': r'^```$',
}


SPECIAL_CHARS = set([
    '*', # bold
    '_', # italic
    '~', # strikethrough
    '`', # code
])



