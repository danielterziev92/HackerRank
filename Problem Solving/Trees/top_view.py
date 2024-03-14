from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    if root is None:
        return

    horizontal_distance = {}

    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()

        if hd not in horizontal_distance:
            horizontal_distance[hd] = node.info

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    for key in sorted(horizontal_distance.keys()):
        print(horizontal_distance[key], end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
