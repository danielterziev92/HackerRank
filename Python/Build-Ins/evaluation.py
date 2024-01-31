import sys
from io import StringIO

test1 = 'print(2 + 3)'

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    eval(input())
