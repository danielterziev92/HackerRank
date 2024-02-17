import sys
from io import StringIO

test1 = '17'

sys.stdin = StringIO(test1)


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal_format = f'{i:>{width}d}'
        octal_format = f'{i:>{width}o}'
        hexadecimal_format = f'{i:>{width}X}'
        binary_format = f'{i:>{width}b}'
        print(decimal_format, octal_format, hexadecimal_format, binary_format)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
