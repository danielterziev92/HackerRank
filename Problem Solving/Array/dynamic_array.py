import sys
from io import StringIO

test1 = '''2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1'''

sys.stdin = StringIO(test1)

import os


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    results = []

    for query in queries:
        q, x, y = query
        if q == 1:
            idx = (x ^ lastAnswer) % n
            seqList[idx].append(y)
        elif q == 2:
            idx = (x ^ lastAnswer) % n
            size = len(seqList[idx])
            lastAnswer = seqList[idx][y % size]
            results.append(lastAnswer)

    return results


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
    print('\n')
