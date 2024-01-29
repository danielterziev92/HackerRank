import sys
from io import StringIO

test1 = '''4
2 4 5 9
4
2 4 11 12'''

test2 = '''2
8 -10
3
5 6 7
'''

sys.stdin = StringIO(test2)

if __name__ == '__main__':
    _ = int(input())
    set_a = set(map(int, input().split()))

    _ = int(input())
    set_b = set(map(int, input().split()))

    result = list(set_a.symmetric_difference(set_b))
    print('\n'.join(map(str, sorted(result, key=lambda x: x))))
