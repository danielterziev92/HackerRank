import sys
from io import StringIO

test1 = '''5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
'''

sys.stdin = StringIO(test1)

from collections import namedtuple
from statistics import mean

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
marks_index = columns.index('MARKS')

print(f'{mean(int(Student(*input().split())[marks_index]) for _ in range(n)):.2f}')
