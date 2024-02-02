import sys
from io import StringIO

test1 = '5'

sys.stdin = StringIO(test1)

cube = lambda x: x ** 3


def fibonacci(n):
    fib_list = [0, 1]
    for _ in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
