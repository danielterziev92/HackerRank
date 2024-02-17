import sys
from io import StringIO

test1 = '''Ross
Taylor'''

sys.stdin = StringIO(test1)


def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
