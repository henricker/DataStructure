"""
Each node needs had "two" children
When the node has no children, 
or has only one, it is complemented 
with "empty nodes"
"""

from Node import Node

class BinaryTree:
  def __init__(self, data = None, node = None):
    if node:
      self.root = node
    elif data:
      node = Node(data)
      self.root = node
    else:
      self.root = None

  #Show all nodes wih inorder traversal algorithm
  def inorder_traversal(self, node=None):
    if node is None:
      node = self.root

    if node.left:
      print('(', end='')
      self.inorder_traversal(node.left)
    
    print(node, end='')

    if node.right:
      self.inorder_traversal(node.right)
      print(')', end='')
  
  #Show all nodes with Post order algorithm
  def postOrder_traversal(self, node = None):
    if node is None:
      node = self.root
    if node.left:
      self.postOrder_traversal(node.left)
    if node.right:
      self.postOrder_traversal(node.right)
    print(node, end='')
  
  #Calculate the heigth using postOrder_traversal
  def height(self, node = None):
    if node is None:
      node = self.root
    heightLeft = 0
    heightRight = 0

    if node.left:
      heightLeft = self.height(node.left)
    if node.right:
      heightRight = self.height(node.right)
    
    if heightRight > heightLeft:
      return heightRight + 1
    return heightLeft + 1
    
    



if __name__ == "__main__":
  tree = BinaryTree(7)
  tree.root.left = Node(18)
  tree.root.right = Node(14)

  print(tree.root)
  print(tree.root.left)
  print(tree.root.right)
  
