import sys
from io import StringIO

test1 = '11 33'

sys.stdin = StringIO(test1)


def door_mat_pattern(rows, cols):
    for i in range(1, rows, 2):
        pattern = '.|.' * i
        print(pattern.center(cols, '-'))

    print('WELCOME'.center(cols, '-'))

    for i in range(rows - 2, 0, -2):
        pattern = '.|.' * i
        print(pattern.center(cols, '-'))


if __name__ == '__main__':
    n, m = map(int, input().split())
    door_mat_pattern(n, m)
