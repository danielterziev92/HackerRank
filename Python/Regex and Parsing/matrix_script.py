import sys
from io import StringIO

test1 = '''7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
'''

sys.stdin = StringIO(test1)

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix = list(zip(*matrix))
encoded = ''.join([''.join(m) for m in matrix])
decoded = re.sub(r'\b\W+\b', ' ', encoded)
print(decoded)
