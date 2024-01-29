import sys
from io import StringIO

test1 = '1+2j'

sys.stdin = StringIO(test1)

import cmath


def polar_coordinates(complex_number):
    r = abs(complex_number)
    phi = cmath.phase(complex_number)
    return r, phi


if __name__ == '__main__':
    complex_number = complex(input())
    r, phi = polar_coordinates(complex_number)

    print(f'{r:.3f}')
    print(f'{phi:.3f}')
