import sys
from io import StringIO

test1 = '5'

sys.stdin = StringIO(test1)

for i in range(1, int(input()) + 1):
    print(((10 ** i) // 9) ** 2)
