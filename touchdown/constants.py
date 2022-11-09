MARKDOWN_REGEXS = {
    # https://www.debuggex.com/r/yJLwFDiFjDuifTSr
    'header': r'^(#{1,6}?) (.*?)$',

    # making this a separate regex from the original header regex
    # to make debugging easier
    # https://www.debuggex.com/r/LuSPWfF7IrFnoG6-
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

    'mathblock': r'^\$\$[\n\r]*?',

    'math': r'\$(.+?)\$',

    # https://www.debuggex.com/r/v_AE_qRrG_tOMTNc
    'paragraph_id': r'^{([a-zA-Z0-9_\-]*)}',

    # https://www.debuggex.com/r/p2CN4H5EZaHe8Fz7
    # this allows for the following types of import statements:
    # 1. import '<FILE>'             can be used for JS and CSS
    # 2. defer import '<FILE>'       can be used for JS and CSS
    # 3. async import '<FILE>'       can be used for JS
    # 4. async defer import <FILE>   cannot be used at all - invalid syntax
    'import': r"(?:(async)?[^\S\r\n]+)?(?:(defer)?[^\S\r\n]+)?import '([A-Za-z0-9-._~:/\?\#\[\]@!\$,&'\(\)\*\+,;%=]+)'[\n\r]*?",

    # NOTE: debbugex cannot render this regex because of the negative lookahead - `(?<!=)`
    # web-component support is in beta - not supported features:
    #   1. Nesting outermost web-component does not work
    #     EX: <test-element>
    #           <test-element>
    #           </test-element>
    #         </test-element>
    'web_component': r'^(<([a-zA-Z]+-[a-zA-Z]+)(.|[\n\r])*?(?<!=)>[\n\r]?(.|[\n\r])*</([a-zA-Z]+-[a-zA-Z]+)>[\n\r]?)$',

    # NOTE: debbugex cannot render this regex because of the negative lookahead - `(?<!=)`
    'web_component_self_closing': r'^(<([a-zA-Z]+-[a-zA-Z]+)(.|[\n\r])*?(?<!=) ?/>)$',
}


SPECIAL_CHARS = set([
    '*', # bold
    '_', # italic
    '~', # strikethrough
    '`', # code
])
