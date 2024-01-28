import sys
from io import StringIO

test1 = '''2
1 2
3 4
1 2
3 4'''

sys.stdin = StringIO(test1)

import numpy

n = int(input())
arr_a = numpy.array([input().split() for _ in range(n)], dtype=int)
arr_b = numpy.array([input().split() for _ in range(n)], dtype=int)

arr = numpy.dot(arr_a, arr_b)

print(arr)
