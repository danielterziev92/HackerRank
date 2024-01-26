import sys
from io import StringIO

test1 = '''3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2'''

sys.stdin = StringIO(test1)

test_cases = int(input())
for _ in range(test_cases):
    elements_count_of_set_a = int(input())
    elements_of_set_a = set(map(int, input().split()))
    elements_count_of_set_b = int(input())
    elements_of_set_b = set(map(int, input().split()))

    if elements_of_set_a.issubset(elements_of_set_b):
        print('True')
        continue

    print('False')
