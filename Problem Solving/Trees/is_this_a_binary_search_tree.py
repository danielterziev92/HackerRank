""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root, prev):
    if root is None:
        return True

    if not is_bst(root.left, prev):
        return False

    if root.data <= prev[0]:
        return False

    prev[0] = root.data

    return is_bst(root.right, prev)


def check_binary_search_tree_(root):
    prev = [float('-inf')]
    return is_bst(root, prev)
