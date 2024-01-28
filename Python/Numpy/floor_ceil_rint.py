import sys
from io import StringIO

test1 = '1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9'

sys.stdin = StringIO(test1)

import numpy

numpy.set_printoptions(legacy='1.13')
arr = numpy.array(input().split(), dtype=float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
