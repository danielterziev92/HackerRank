import sys
from io import StringIO

test1 = '''1 2 3 4 -8 -10'''

sys.stdin = StringIO(test1)

import numpy


def arrays(arr):
    numpy_arr = numpy.array(arr, dtype=float)
    return numpy.flip(numpy_arr)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
