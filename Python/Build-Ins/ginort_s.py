import sys
from io import StringIO

test1 = 'Sorting1234'

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    s = input()
    sorted_str = ''.join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x)))
    print(sorted_str)
