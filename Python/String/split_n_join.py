import sys
from io import StringIO

test1 = 'this is a string'

sys.stdin = StringIO(test1)


def split_and_join(line):
    return '-'.join(line.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
