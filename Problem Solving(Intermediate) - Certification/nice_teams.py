import sys
from io import StringIO

test1 = '''4
1
1
1
1
1'''

test2 = '''6
3
4
5
2
1
1
3'''

test3 = '''6
1
2
3
4
5
6
4'''

sys.stdin = StringIO(test2)

from itertools import combinations


def maxPairs(skillLevel, minDiff):
    skillLevel.sort()
    n = len(skillLevel)
    i = 0
    x = []

    for j in range(n // 2):
        while i < n and skillLevel[i] - skillLevel[j] < minDiff:
            i += 1
        if i >= n:
            break
        x.append(i)
    x = x[:(n // 2)]

    pairs = 0
    k = n - 1
    for y in reversed(x):
        if y <= k:
            pairs += 1
            k -= 1

    return pairs


'The coach would like to pair up students whose ratings differ by no less than a given minimum.'

if __name__ == '__main__':
    skillLevel_count = int(input().strip())

    skillLevel = []

    for _ in range(skillLevel_count):
        skillLevel_item = int(input().strip())
        skillLevel.append(skillLevel_item)

    minDiff = int(input().strip())

    result = maxPairs(skillLevel, minDiff)

    print(str(result) + '\n')
