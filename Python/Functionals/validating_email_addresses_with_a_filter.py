import sys
from io import StringIO

test1 = '''2 1
5 6'''

sys.stdin = StringIO(test1)

from re import match


def fun(s):
    pattern = r'^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return bool(match(pattern, s))


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
