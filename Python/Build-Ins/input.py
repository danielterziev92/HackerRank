import sys
from io import StringIO

test1 = '''1 4
x**3 + x**2 + x + 1'''

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    x, y = map(int, input().split())
    result = eval(input())
    if result == y:
        print(True)
    else:
        print(False)
