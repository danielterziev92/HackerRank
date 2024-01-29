import sys
from io import StringIO

test1 = '''3
4
5'''

sys.stdin = StringIO(test1)

a, b, m = int(input()), int(input()), int(input())
print(pow(a, b))
print(pow(a, b, m))
