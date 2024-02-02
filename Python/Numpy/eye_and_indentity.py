import sys
from io import StringIO

test1 = '3 3'

sys.stdin = StringIO(test1)

import numpy

shape = tuple(map(int, input().split()))
numpy.set_printoptions(legacy='1.13')
arr_identity = numpy.eye(*shape, k=0)
print(arr_identity)
