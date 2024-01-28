import sys
from io import StringIO

test1 = '''aaadaa
aa'''

sys.stdin = StringIO(test1)

import re


def find_start_end_indices(string, substring):
    pattern = re.compile(f'(?=({re.escape(substring)}))')
    matches = list(pattern.finditer(string))

    if not matches:
        print((-1, -1))
    else:
        for match in matches:
            start_index = match.start(1)
            end_index = match.end(1) - 1
            print((start_index, end_index))


if __name__ == "__main__":
    main_string = input()

    substring = input()

    find_start_end_indices(main_string, substring)
