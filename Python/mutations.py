import sys
from io import StringIO

test1 = '''16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
'''

sys.stdin = StringIO(test1)

_ = int(input())
elements = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command, *_ = input().split()
    getattr(elements, command)(set(map(int, input().split())))

print(sum(elements))
