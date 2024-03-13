import sys
from io import StringIO

test1 = '''1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0'''

sys.stdin = StringIO(test1)

import math
import os
import random
import re
import sys


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    def hourglass_sum(row, col):
        return (
                arr[row][col] + arr[row][col + 1] + arr[row][col + 2] +
                arr[row + 1][col + 1] +
                arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
        )

    max_sum = float('-inf')

    for row in range(len(arr) - 2):
        for col in range(len(arr[0]) - 2):
            current_sum = hourglass_sum(row, col)
            max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result) + '\n')
