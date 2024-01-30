import sys
from io import StringIO

test1 = '''4
4.0O0
-1.00
+4.54
SomeRandomStuff'''

sys.stdin = StringIO(test1)

import re


def is_valid_email(email):
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern, email))


if __name__ == '__main__':
    n = int(input())
    emails = [input().strip() for _ in range(n)]

    [print(is_valid_email(email)) for email in emails]
