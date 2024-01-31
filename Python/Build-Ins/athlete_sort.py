import sys
from io import StringIO

test1 = '''5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1'''

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    n, _ = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sorted_idx = int(input())
    result = sorted(arr, key=lambda x: x[sorted_idx])
    [print(*x, sep=' ') for x in result]
