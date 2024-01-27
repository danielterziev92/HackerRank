import sys
from io import StringIO

test1 = 'HACK 2'

sys.stdin = StringIO(test1)

from itertools import combinations_with_replacement


def get_combinations_with_replacement(text, size):
    return sorted(map(lambda x: ''.join(sorted(x)), combinations_with_replacement(text, size)))


if __name__ == '__main__':
    text, size = input().split()

    all_combinations = get_combinations_with_replacement(text, int(size))

    print(*all_combinations, sep='\n')
