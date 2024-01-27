import sys
from io import StringIO

test1 = '1222311'

sys.stdin = StringIO(test1)

from itertools import groupby

if __name__ == '__main__':
    input_data = map(int, list(input()))

    groups = [(len(list(g)), int(k)) for k, g in groupby(input_data)]
    result = ' '.join(f'({count}, {digit})' for count, digit in groups)
    print(result)
