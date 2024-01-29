import sys
from io import StringIO

test1 = '''177
10'''

sys.stdin = StringIO(test1)

result = divmod(int(input()), int(input()))
[print(x) for x in result]
print(result)
