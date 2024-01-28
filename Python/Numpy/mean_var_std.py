import sys
from io import StringIO

test1 = '''2 2
1 2
3 4'''

sys.stdin = StringIO(test1)

import numpy

n, m = map(int, input().split())

arr = numpy.array([input().split() for _ in range(n)], dtype=int)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))
