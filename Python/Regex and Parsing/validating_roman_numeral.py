import sys
from io import StringIO

test1 = 'CDXXI'

sys.stdin = StringIO(test1)

import re


def is_valid_roman_numeral(s):
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    return bool(re.match(pattern, s))


if __name__ == "__main__":
    roman_numeral = input()

    print(is_valid_roman_numeral(roman_numeral))
