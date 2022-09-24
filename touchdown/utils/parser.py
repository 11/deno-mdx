def lookahead(pattern, substr):
    """ lookahead determines if a pattern shows up in a string

    TODO: this function does not correctly handle all escape character scenarios.
          as an example, if we called `lookahead` with the following inputs:

            pattern = '*'
            substr = 'this is a test string \\*'

          the double backslash before the * is escaping the backslash
          character, NOT the * character. in the current implementation
          this would incorrectly assum the * character is being escaped.
          this edge case is pretty rare and can mostly be ignored - but
          should eventually be resolved later
    """
    next_idx = substr.find(pattern)
    if next_idx == -1:
        # return false if there is no closing pattern
        return False

    lag = substr[:next_idx]
    if len(lag) == 0:
        # if there are zero characters before the closing patter, this it's
        # not possible for the pattern to be escaped. therefore, it's always
        # a valid closing pattern
        return True
    elif len(lag) == 1 and substr[next_idx-1] == '\\':
        # if the closing pattern is escaped with a `\` character, then
        # that means the closing pattern should not be considered Mardown
        # syntax, but rather an actual character that belonds in the text.
        return False

    return True


def map_decorations_to_tokens(decorations: set):
    """ return correct token and tag values for text blocks wrapped in decorations """

    decors_token_map = {
        '*': 'bold',
        '_': 'italic',
        '~': 'strikethrough',
        '`': 'code',
    }

    decors_tag_map = {
        '*': 'b',
        '_': 'i',
        '~': 's',
        '`': 'code',
    }

    # sets in python do not append in the same order every time.
    # to ensure that decorations are applied in a the same order
    # each time we sort the set of decorations
    decorations = sorted(decorations)

    return {
        'token': [decors_token_map[decor] for decor in decorations],
        'tag': [decors_tag_map[decor] for decor in decorations],
    }


def create_html_tag_id(tag_id: str):
    """ alphanumerics, `-`, and `_` are the only valid characters in a html ID """

    # filter string to only contain valid characters for an id
    sanitize_valid_chars = lambda char: \
        char.isalpha() \
        or char.isnumeric() \
        or char in ['_', '-', ' ']
    valid_chars = ''.join(filter(sanitize_valid_chars, tag_id))


    # strip any extra whitespace between each word
    strip_whitespace = list(map(lambda word: word.strip(), valid_chars.split(' ')))

    # strip empty strings
    strip_empty_strings = list(filter(lambda word: word != '', strip_whitespace))

    # place a `-` between each valid collection of words
    valid_id = '-'.join(strip_empty_strings)

    return valid_id
