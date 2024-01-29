import sys
from io import StringIO

test1 = ''' 1 2
 3 4
'''

sys.stdin = StringIO(test1)

from itertools import product

print(*list(product(list(map(int, input().split())), list(map(int, input().split())))))
