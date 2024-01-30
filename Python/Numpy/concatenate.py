import sys
from io import StringIO

test1 = '''4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4'''

sys.stdin = StringIO(test1)

from numpy import concatenate

n, m, p = map(int, input().split())
arr_a = [list(map(int, input().split())) for _ in range(n)]
arr_b = [list(map(int, input().split())) for _ in range(m)]
print(concatenate((arr_a, arr_b)))
