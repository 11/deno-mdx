MARKDOWN_REGEXS = {
    # https://www.debuggex.com/r/yJLwFDiFjDuifTSr
    'header': r'^(#{1,6}?) (.*?)$',

    # https://www.debuggex.com/r/CtnsXDb7jI1pMumX
    'blockquote': r'^\> [\s]*(.*)$',

    # https://www.debuggex.com/r/s2BZUI9PedP0m5O-
    'ordered_list': r'^\s*[0-9]{1,}. ([\s\S]*)\n$',

    # https://www.debuggex.com/r/9hQERKefFNj_3CsR
    'unordered_list': r'^\s*- ([\s\S]*)\n$',

    # https://www.debuggex.com/r/u64sYbgHehYd5zet
    'image': r'^!\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/dnmmbV9HXMOBFQPa
    'link': r'^\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/dB-xS-Jo6RGl9NW2
    'codeblock_header': r'^(```)[\s]*?([a-zA-Z1-9]*)[\s]*?[\n\r]',

    # https://www.debuggex.com/r/hEMpYtUnAaOJO-At
    'codeblock_footer': r'^```[\n\r]*?',

    # TODO: need to add support for latex math syntax
    'math': r'r\$\$$',
}


SPECIAL_CHARS = set([
    '*', # bold
    '_', # italic
    '~', # strikethrough
    '`', # code
])
