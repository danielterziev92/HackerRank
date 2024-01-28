import sys
from io import StringIO

test1 = '''1.1 2 3
0'''

sys.stdin = StringIO(test1)

import numpy

arr = numpy.array(input().split(), dtype=float)
value = int(input())
poly_arr = numpy.polyval(arr, value)
print(poly_arr)
