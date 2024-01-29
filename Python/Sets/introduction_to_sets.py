import sys
from io import StringIO

test1 = '''10
161 182 161 154 176 170 167 171 170 174
'''

sys.stdin = StringIO(test1)


def average(array):
    array = set(array)
    return sum(array) / len(array)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
