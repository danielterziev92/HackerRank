import sys
from io import StringIO

test1 = '''2
B1CD102354
B1CDEF2354
'''

sys.stdin = StringIO(test1)

import re


def is_valid_uid(uid):
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False

    if len(re.findall(r'\d', uid)) < 3:
        return False

    if len(uid) != len(set(uid)):
        return False

    if len(uid) != 10:
        return False

    return True


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        uid = input()
        if is_valid_uid(uid):
            print("Valid")
        else:
            print("Invalid")
