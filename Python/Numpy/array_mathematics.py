import sys
from io import StringIO

test1 = '''1 4
1 2 3 4
5 6 7 8'''

sys.stdin = StringIO(test1)

import numpy

n, m = map(int, input().split())

a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)

add_result = numpy.add(a, b)
subtract_result = numpy.subtract(a, b)
multiply_result = numpy.multiply(a, b)
divide_result = numpy.floor_divide(a, b)
mod_result = numpy.mod(a, b)
power_result = numpy.power(a, b)

print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_result)
print(mod_result)
print(power_result)
