import sys
from io import StringIO

test1 = '''2
.*\+
.*+'''

sys.stdin = StringIO(test1)

import re


def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        if '*+' in pattern or '+?' in pattern or '++' in pattern:
            return False

        return True
    except Exception:
        return False


rows = int(input())
patterns = [input() for _ in range(rows)]

for pattern in patterns:
    print(is_valid_regex(pattern))
