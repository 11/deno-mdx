MARKDOWN_REGEXS = {
    # https://www.debuggex.com/r/yJLwFDiFjDuifTSr
    'header': r'^(#{1,6}?) (.*?)$',

    # https://www.debuggex.com/r/LuSPWfF7IrFnoG6-
    # making this a separate regex from the original header regex
    # to make debugging easier
    'header_id': r'^(#{1,6}?) {([a-zA-Z0-9_\-]*)} (.*?)$',

    # https://www.debuggex.com/r/CtnsXDb7jI1pMumX
    'blockquote': r'^\> [\s]*(.*)$',

    # https://www.debuggex.com/r/lpCTo47Zcrchtin0
    'ordered_list': r'^\s*[0-9]{1,}. (.*)[\n\r]?$',

    # https://www.debuggex.com/r/UUuIqZUx6MX5gnPj
    'unordered_list': r'^\s*- (.*)[\n\r]?$',

    # https://www.debuggex.com/r/u64sYbgHehYd5zet
    'image': r'^!\[(.*)\]\((.*)\)$',

    # https://www.debuggex.com/r/R5GTdhmtm06W8MZj
    'link': r'\[(.+?)\]\((.+?)\)',

    # https://www.debuggex.com/r/dB-xS-Jo6RGl9NW2
    'codeblock_header': r'^(```)[\s]*?([a-zA-Z1-9]*)[\s]*?[\n\r]',

    # https://www.debuggex.com/r/hEMpYtUnAaOJO-At
    'codeblock_footer': r'^```[\n\r]*?',

    # TODO: need to add support for latex math syntax
    'math': r'r\$\$$',

    # https://www.debuggex.com/r/v_AE_qRrG_tOMTNc
    'paragraph_id': r'^{([a-zA-Z0-9_\-]*)}',
}


SPECIAL_CHARS = set([
    '*', # bold
    '_', # italic
    '~', # strikethrough
    '`', # code
])
