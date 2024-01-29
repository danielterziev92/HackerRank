import sys
from io import StringIO

test1 = '''3
1 0
2 $
3 1'''

sys.stdin = StringIO(test1)

rows = int(input())

for _ in range(rows):
    a, b = input().split(' ')

    try:
        print(int(int(a) // int(b)))
    except (ZeroDivisionError, ValueError) as e:
        print(f'Error Code: {e}')
