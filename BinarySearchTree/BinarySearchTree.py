"""
  Binary search tree

  properties:
    Each child node smaller than the parent node is on the left
    Each child node greater than the parent node is on the right

"""
from BinaryTree import BinaryTree

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
  def __str__(self):
    return str(self.data)


class BinarySearchTree(BinaryTree):
  
  def insert(self, value):
    parent = None
    iterator = self.root

    while iterator:
      parent = iterator
      if value < iterator.data:
        iterator = iterator.left
      else:
        iterator = iterator.right
      
    if parent is None:
      self.root = Node(value)
    elif value < parent.data:
      parent.left = Node(value)
    else:
      parent.right = Node(value)
  
  #Search algorithm in BST
  def search(self, value):
    return self._search(value, self.root)

  def _search(self, value, node):
    if node is None:
      return node
    if node.data == value:
      return BinarySearchTree(node)
    if value < node.data:
      return self._search(value, node.left)
    return self._search(value, node.right)

      
