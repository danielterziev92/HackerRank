import sys
from io import StringIO

test1 = '''5 4
1 2 3 4 5'''

sys.stdin = StringIO(test1)

import math
import os
import random
import re
import sys


#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    n = len(arr)
    d = d % n

    rotated = [None] * n

    for i in range(n):
        new_index = (i - d) % n
        rotated[new_index] = arr[i]

    return rotated


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    print(' '.join(map(str, result)))
    print('\n')
