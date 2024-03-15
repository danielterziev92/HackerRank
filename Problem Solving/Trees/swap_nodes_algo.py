#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def swapNodes(indexes, queries):
    def buildTree(indexes):
        nodes = [Node(i) for i in range(len(indexes) + 1)]
        for i, (left, right) in enumerate(indexes, start=1):
            if left != -1:
                nodes[i].left = nodes[left]
            if right != -1:
                nodes[i].right = nodes[right]
        return nodes[1]  # Return the root node

    def inOrderTraversal(root):
        result = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.data)
                node = node.right
        return result

    def swapSubtrees(root, k, depth):
        if root is None:
            return
        if depth % k == 0:
            root.left, root.right = root.right, root.left
        swapSubtrees(root.left, k, depth + 1)
        swapSubtrees(root.right, k, depth + 1)

    root = buildTree(indexes)
    results = []

    for k in queries:
        swapSubtrees(root, k, 1)
        result = inOrderTraversal(root)
        results.append(result)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
