import sys
from io import StringIO

test1 = '''2
9587456281
72252478965
'''

sys.stdin = StringIO(test1)

import re

n = int(input())

for _ in range(n):
    number = input()
    print('YES') if re.match(r'^[789]\d{9}', number) and len(number) == 10 else print('NO')
