import re


def get_matches_for_pattern(pattern, string):
    """
    Get the matches for the pattern.
    :param pattern:
    :param string:
    :return:
    """
    matches = pattern.findall(string)
    return [match[0] for match in matches]


product_review = '''This is a fine milk, but the product
                    line appears to be limited in available colors. I
                    could only find white.'''

# Split into sentences
sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
sentences = get_matches_for_pattern(pattern=sentence_pattern, string=product_review)

# Split into tokens
word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    words = get_matches_for_pattern(pattern=word_pattern, string=sentence)
    print(f'{words}')
