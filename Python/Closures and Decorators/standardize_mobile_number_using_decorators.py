import sys
from io import StringIO

test1 = '''3
07895462130
919875641230
9195969878'''

test2 = '''3
09191919191
9100256236
+919593621456'''

sys.stdin = StringIO(test2)

from re import match


def wrapper(f):
    def fun(l):
        pattern = r'^([+]*\d{1,5})*(\d{5})(\d{5})$'
        numbers = list()
        for phone in l:
            numb = match(pattern, phone)
            if numb:
                numbers.append(f"+91 {numb.group(2)} {numb.group(3)}")

        numbers.sort(key=lambda x: x)

        return f(numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
