import sys
from io import StringIO

test1 = '''1 2 3 4 5 6 7 8 9'''

sys.stdin = StringIO(test1)

import numpy

arr = list(map(int, input().split()))
print(numpy.array(arr).reshape(3, 3))
