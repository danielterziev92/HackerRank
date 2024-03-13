import sys
from io import StringIO

test1 = '''5 3
1 2 100
2 5 100
3 4 100'''

sys.stdin = StringIO(test1)

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for query in queries:
        a, b, k = query
        arr[a - 1] += k
        arr[b] -= k

    max_value = 0
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        max_value = max(max_value, current_sum)

    return max_value


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
