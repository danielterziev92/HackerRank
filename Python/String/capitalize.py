import sys
from io import StringIO

test1 = 'chris alan'
test2 = '1 w 2 r 3g'

sys.stdin = StringIO(test1)


def solve(s):
    return ' '.join([word.title() if word[:1].isalpha() else word for word in s.split()])


if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
