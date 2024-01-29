import sys
from io import StringIO

test1 = '''9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5'''

sys.stdin = StringIO(test1)

_ = int(input())
elements = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    command, *num = input().strip().split()
    getattr(elements, command)(*map(int, num))

print(sum(elements))
