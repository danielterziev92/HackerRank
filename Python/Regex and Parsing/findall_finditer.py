import sys
from io import StringIO

test1 = '''rabcdeefgyYhFjkIoomnpOeorteeeeet'''

sys.stdin = StringIO(test1)

import re


def find_vowel_substrings(s):
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
    matches = re.findall(pattern, s)

    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)


if __name__ == "__main__":
    s = input().strip()
    find_vowel_substrings(s)
