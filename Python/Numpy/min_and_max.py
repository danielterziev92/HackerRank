import sys
from io import StringIO

test1 = '''4 2
2 5
3 7
1 3
4 0'''

sys.stdin = StringIO(test1)

import numpy

n, m = map(int, input().split())
matrix = numpy.array([input().split() for _ in range(n)], dtype=int)
matrix_axis_1 = numpy.min(matrix, axis=1)
max_numb = numpy.max(matrix_axis_1)
print(max_numb)
