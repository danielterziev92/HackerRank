import sys
from io import StringIO

test1 = '''4
bcdef
abcdefg
bcde
bcdef'''

sys.stdin = StringIO(test1)

from collections import OrderedDict


def count_word_occurrences(words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


n = int(input().strip())
word_list = [input().strip() for _ in range(n)]

word_occurrences = count_word_occurrences(word_list)

print(len(word_occurrences))
print(*word_occurrences.values())
