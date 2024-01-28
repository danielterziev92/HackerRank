import sys
from io import StringIO

test1 = '''0 1
2 3'''

sys.stdin = StringIO(test1)

import numpy

arr_a = numpy.array(input().split(), dtype=int)
arr_b = numpy.array(input().split(), dtype=int)
inner_array = numpy.inner(arr_a, arr_b)
outer_array = numpy.outer(arr_a, arr_b)

print(inner_array)
print(outer_array)
