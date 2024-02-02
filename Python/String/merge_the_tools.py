import sys
from io import StringIO

test1 = '''AABCAAADA
3'''

sys.stdin = StringIO(test1)


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        unique_chars = ''.join(sorted(set(substring), key=substring.index))
        print(unique_chars)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
