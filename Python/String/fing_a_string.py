import sys
from io import StringIO

test1 = '''ABCDCDC
CDC'''

sys.stdin = StringIO(test1)


def count_substring(string, sub_string):
    result = 0
    for i in range(len(string)):
        if string[i: i + len(sub_string)] == sub_string:
            result += 1

    return result


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
