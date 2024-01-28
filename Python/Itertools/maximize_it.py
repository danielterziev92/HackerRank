import sys
from io import StringIO

test1 = '''3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10'''

sys.stdin = StringIO(test1)

from itertools import product


def maximize_expression(arrays, m):
    combinations = list(product(*arrays))

    max_value = max(sum(x ** 2 for x in combo) % m for combo in combinations)

    return max_value


if __name__ == "__main__":
    n, m = map(int, input().split())

    arrays = [list(map(int, input().split()[1:])) for _ in range(n)]

    result = maximize_expression(arrays, m)
    print(result)
