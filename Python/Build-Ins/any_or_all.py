import sys
from io import StringIO

test1 = '''5
12 9 61 5 14'''

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    _ = input()
    arr = list(map(int, input().split()))
    result = list()

    if all(num > 0 for num in arr):
        result.append(True)
    else:
        result.append(False)

    if any(str(num) == str(num)[::-1] for num in arr):
        result.append(True)
    else:
        result.append(False)

    print(all(result))
