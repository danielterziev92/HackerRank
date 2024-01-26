import sys
from io import StringIO

test1 = '''2
1 2
'''

sys.stdin = StringIO(test1)

rows = int(input())
data = map(int, input().split())
print(hash(data))
