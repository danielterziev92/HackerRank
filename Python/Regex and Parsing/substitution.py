import sys
from io import StringIO

test1 = '''11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.'''

sys.stdin = StringIO(test1)

import re

if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        x = input()
        repl_or = re.sub(r'\s\|\|\s', ' or ', x)
        repl_or = re.sub(r'\s\|\|\s', ' or ', repl_or)
        repl_and = re.sub(r'\s&&\s', ' and ', repl_or)
        print(re.sub(r'\s&&\s', ' and ', repl_and))
