import sys
from io import StringIO

test1 = '''4
1 4 3 2'''

sys.stdin = StringIO(test1)

import math
import os
import random
import re
import sys


def reverseArray(a):
    return reversed(a)


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
