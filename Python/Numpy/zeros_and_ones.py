import sys
from io import StringIO

test1 = '3 3 3'

sys.stdin = StringIO(test1)

import numpy

shape = tuple(map(int, input().split()))

zeros_array = numpy.zeros(shape, dtype=int)
ones_array = numpy.ones(shape, dtype=int)

print(zeros_array)
print(ones_array)
