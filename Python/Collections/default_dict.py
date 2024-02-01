import sys
from io import StringIO

test1 = '''5 2
a
a
b
a
b
a
b'''

sys.stdin = StringIO(test1)

from collections import defaultdict


def word_indices(n, m, list_a, list_b):
    indices = defaultdict(list)
    for i, word in enumerate(list_a):
        indices[word].append(i + 1)

    for word in group_b:
        if word in indices:
            print(*indices[word], sep=' ')
        else:
            print('-1')


size_a, size_b = map(int, input().split())
group_a = [input() for _ in range(size_a)]
group_b = [input() for _ in range(size_b)]

word_indices(size_a, size_b, group_a, group_b)
