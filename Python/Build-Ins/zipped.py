import sys
from io import StringIO

test1 = '''5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5'''

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = [input().split() for _ in range(m)]
    zip_arr = list(zip(*arr))
    [print(f'{sum(list(map(float, x))) / len(x):.1f}') for x in zip_arr]
