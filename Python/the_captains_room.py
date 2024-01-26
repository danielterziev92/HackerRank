import sys
from io import StringIO

test1 = '''5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
'''

sys.stdin = StringIO(test1)

group_size = int(input())
room_numbers = list(map(int, input().split()))

unique_rooms = set(room_numbers)
for room in room_numbers:
    if len(unique_rooms) == 1:
        break

    if room in unique_rooms:
        unique_rooms.remove(room)

print(unique_rooms.pop())
