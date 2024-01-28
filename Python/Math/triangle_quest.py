import sys
from io import StringIO

test1 = '5'

sys.stdin = StringIO(test1)

for i in range(1, int(input())):
    print(((10 ** i - 1) // 9) * i)
