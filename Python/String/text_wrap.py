import sys
from io import StringIO

test1 = '''ABCDEFGHIJKLIMNOQRSTUVWXYZ
4'''

sys.stdin = StringIO(test1)

import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
