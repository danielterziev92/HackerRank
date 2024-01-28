import sys
from io import StringIO

test1 = '''2
1.1 1.1
1.1 1.1'''

sys.stdin = StringIO(test1)

import numpy

n = int(input())
arr = numpy.array([input().split() for _ in range(n)], dtype=float)

print(round(numpy.linalg.det(arr), 2))
