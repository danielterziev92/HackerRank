import sys
from io import StringIO

test1 = '''3 2
1 5 3
3 1
5 7'''

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    elements = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    happiness = 0

    for el in elements:
        if el in set_a:
            happiness += 1

        elif el in set_b:
            happiness -= 1

    print(happiness)
