import sys
from io import StringIO

test1 = '2 5'

sys.stdin = StringIO(test1)


def avg(*args):
    return sum(args) / len(args)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    res = avg(*nums)
    print(res)
