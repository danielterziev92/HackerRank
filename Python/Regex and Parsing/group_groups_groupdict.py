import sys
from io import StringIO

test1 = '''..12345678910111213141516171820212223'''

sys.stdin = StringIO(test1)

import re


def find_repeating_character(s):
    match = re.search(r'([a-zA-Z0-9])\1', s)
    if match:
        return match.group(1)
    else:
        return -1


if __name__ == '__main__':
    s = input()
    result = find_repeating_character(s)
    print(result)
