import sys
from io import StringIO

test1 = '''2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
'''

sys.stdin = StringIO(test1)

import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)


def print_valid_pairs(email_pairs):
    for name, email in email_pairs:
        if is_valid_email(email):
            print(f'{name} <{email}>')


if __name__ == '__main__':
    n = int(input())

    email_pairs = []
    for _ in range(n):
        line = input().split()
        name = line[0]
        email = line[1][1:-1]
        email_pairs.append((name, email))

    print_valid_pairs(email_pairs)
