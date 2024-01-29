import sys
from io import StringIO

test1 = '3'

sys.stdin = StringIO(test1)


def print_rangoli(size):
    alphas = list()
    cols = size + (size - 1) * 3
    for i in range(size - 1, 0, -1):
        alpha = chr(i + ord('a'))
        pattern = alphas + list(alpha) + alphas[::-1]
        alphas.append(alpha)
        print('-'.join(pattern).center(cols, '-'))

    alphas.append('a')
    pattern = alphas + alphas[::-1][1:]
    print('-'.join(pattern))

    for i in range(size - 1):
        alphas.pop()
        pattern = alphas + alphas[::-1][1:]
        print('-'.join(pattern).center(cols, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
