import sys
from io import StringIO

test1 = '''2
6
4 3 2 1 3 4
3
1 3 2'''

sys.stdin = StringIO(test1)

from collections import deque


def can_stack_cubes(cubes):
    cube_pile = deque(cubes)
    current_cube = float('inf')

    while cube_pile:
        leftmost = cube_pile.popleft() if cube_pile[0] >= cube_pile[-1] else cube_pile.pop()
        if leftmost > current_cube:
            return "No"
        current_cube = leftmost

    return "Yes"


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    cubes = list(map(int, input().split()))

    result = can_stack_cubes(cubes)

    print(result)
