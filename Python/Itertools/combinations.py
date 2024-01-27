import sys
from io import StringIO

test1 = 'HACK 2'

sys.stdin = StringIO(test1)

from itertools import combinations


def generate_combinations(text, size):
    return sorted(map(lambda x: ''.join(sorted(x)), combinations(text, size)))


if __name__ == "__main__":
    input_data = input().split()
    text = input_data[0]
    size = int(input_data[1])

    all_combinations = list()
    for i in range(1, size + 1):
        result = generate_combinations(text, i)
        all_combinations.extend(result)

    print(*all_combinations, sep='\n')
