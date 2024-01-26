import sys
from io import StringIO

test1 = '''7
UK
China
USA
France
New Zealand
UK
France'''

sys.stdin = StringIO(test1)

n = int(input())

countries = set()
for _ in range(n):
    country = input()
    countries.add(country)

print(len(countries))
