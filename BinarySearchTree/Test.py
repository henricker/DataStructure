from BinarySearchTree import BinarySearchTree
import random

random.seed(66)

def random_tree(size=42):
    values = random.sample(range(1, 1000), 42)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def searchItems(items, bst):
  print('\n-----')
  for item in items:
      r = bst.search(item)
      if r is None:
          print(item, "não encontrado")
      else:
          print(r.root.data, 'encontrado')
  
def example_tree():
  values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
  tree = BinarySearchTree()
  for v in values:
      tree.insert(v)
  return tree




bst = example_tree()

print("------ Inorder traversal -----------")
bst.inorder_traversal()
print()

print("------ Level order traversal -------")
bst.levelorder_traversal()
print()

print("------ Post order traversal ---------")
bst.postorder_traversal()
print()



# bst = random_tree()
# bst.inorder_traversal()
# print()
# print(bst.root)
# print()
# searchItems([73, 32, 23, 518, 949], bst)


