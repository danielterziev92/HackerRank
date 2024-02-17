import sys
from io import StringIO

test1 = 'HackerRank.com presents "Pythonist 2".'

sys.stdin = StringIO(test1)


def swap_case(s):
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
