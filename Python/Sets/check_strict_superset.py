import sys
from io import StringIO

test1 = '''1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
'''

sys.stdin = StringIO(test1)

set_a = set(map(int, input().split()))
n = int(input())

set_b = set()

result = True
for _ in range(n):
    set_b = set(map(int, input().split()))

    if not set_a.issuperset(set_b):
        result = False
        break

print(result)
