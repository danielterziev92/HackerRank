import sys
from io import StringIO

test1 = '''9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8'''

sys.stdin = StringIO(test1)

_ = int(input())
a = set(map(int, input().split()))
_ = int(input())
b = set(map(int, input().split()))

print(len(a.intersection(b)))
