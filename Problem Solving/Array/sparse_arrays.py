import sys
from io import StringIO

test1 = '''4
aba
baba
aba
xzxb
3
aba
xzxb
ab'''

test3 = '''13
abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf
5
abcde
sdaklfj
asdjf
na
basdn'''

sys.stdin = StringIO(test3)

import math
import os
import random
import re
import sys


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    all_occurrences = []

    for query in queries:
        occurrences = [i for i, x in enumerate(stringList) if x == query]
        all_occurrences.append(len(occurrences))

    return all_occurrences


if __name__ == '__main__':
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    print('\n'.join(map(str, res)))
    print('\n')
