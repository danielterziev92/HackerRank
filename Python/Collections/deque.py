import sys
from io import StringIO

test1 = '''6
append 1
append 2
append 3
appendleft 4
pop
popleft'''

sys.stdin = StringIO(test1)

from collections import deque

n = int(input())

queue_list = deque()
for _ in range(n):
    line = input().split()

    command, *data = line

    if command == 'appendleft':
        queue_list.appendleft(*list(map(int, data)))
    elif command == 'append':
        queue_list.append(*list(map(int, data)))
    elif command == 'pop':
        queue_list.pop()
    elif command == 'popleft':
        queue_list.popleft()

print(*queue_list, sep=' ')
