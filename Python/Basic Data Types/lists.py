import sys
from io import StringIO

test1 = '''12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

sys.stdin = StringIO(test1)


def list_funcs(matrix: list, command: str, *args) -> list:
    match command:
        case 'insert':
            idx, arg = args
            matrix.insert(idx, arg)
        case 'print':
            print(matrix)
        case 'remove':
            matrix.remove(args[0])
        case 'append':
            matrix.append(args[0])
        case 'sort':
            matrix.sort(key=lambda x: x)
        case 'pop':
            matrix.pop()
        case 'reverse':
            matrix.reverse()

    return matrix


rows = int(input())

matrix = []
for _ in range(rows):
    command, *params = input().split(' ')
    list_funcs(matrix, command, *map(int, params))
