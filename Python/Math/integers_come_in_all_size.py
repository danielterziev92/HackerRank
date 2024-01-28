import sys
from io import StringIO

test1 = '''9
29
7
27'''

sys.stdin = StringIO(test1)

a, b, c, d = [int(input()) for _ in range(4)]
result = int(a ** b + c ** d)
print(result)
