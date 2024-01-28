import sys
from io import StringIO

test1 = '''2 2
1 2
3 4'''

sys.stdin = StringIO(test1)

import numpy

n, m = input().split()

matrix = numpy.array([input().split() for _ in range(int(n))], dtype=int)
sux_axios_0 = numpy.sum(matrix, axis=0)
result = numpy.prod(sux_axios_0)
print(result)
