import sys
from io import StringIO

test1 = 'HACK 2'

sys.stdin = StringIO(test1)

from itertools import permutations


def generate_permutations(s, size):
    for perm in sorted(permutations(s, size)):
        print(''.join(perm))


if __name__ == "__main__":
    input_data = input().split()
    s = input_data[0]
    size = int(input_data[1])

    generate_permutations(s, size)
