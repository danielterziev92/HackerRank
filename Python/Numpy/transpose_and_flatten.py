import sys
from io import StringIO

test1 = '''2 2
1 2
3 4'''

sys.stdin = StringIO(test1)

import numpy

n, _ = list(map(int, input().split()))
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.transpose(arr))
print(arr.flatten())
