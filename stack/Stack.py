
from Node import Node

class Stack:

  def __init__(self):
    self._size = 0
    self._top = None

  def push(self, data):
    node = Node(data)
    node.next = self._top
    self._top = node
    self._size = self._size + 1
  
  def pop(self):
    if(self._size == 0):
      raise IndexError("Stack is empty!");
    node = self._top
    self._top = self._top.next
    self._size = self._size - 1
    return node.data
  
  def empty(self):
    return self._size == 0
  
  def __len__(self):
    return self._size
  
  def __repr__(self):
    r = ""
    pointer = self._top
    while(pointer):
      r = r + str(pointer.data) + "\n"
      pointer = pointer.next
    return r
  
  def __str__(self):
    return self.__repr__()

  
