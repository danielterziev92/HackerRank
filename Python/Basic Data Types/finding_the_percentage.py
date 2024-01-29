import sys
from io import StringIO

test1 = '''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika'''

sys.stdin = StringIO(test1)

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

all_marks = student_marks[query_name]
average_sum = sum(all_marks) / len(all_marks)

print(f'{average_sum:.2f}')
