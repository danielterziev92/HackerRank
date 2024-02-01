import sys
from io import StringIO

test1 = 'aabbbccde'

sys.stdin = StringIO(test1)

from collections import Counter


def top_three_characters(s):
    char_count = Counter(s)

    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")


if __name__ == '__main__':
    company_name = input()

    top_three_characters(company_name)
