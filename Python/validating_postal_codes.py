import sys
from io import StringIO

test1 = '110000'

sys.stdin = StringIO(test1)

import re

regex_integer_in_range = r'^[1-9]\d{5}$'

regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'

if __name__ == "__main__":
    P = input()

    result = (
            bool(re.match(regex_integer_in_range, P)) and
            len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
    )

    print(result)
