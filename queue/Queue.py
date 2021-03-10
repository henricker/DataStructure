from Node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, data):
        node = Node(data)

        if(self._size == 0):
          self._front = node
          self._back = node
          self._size = 1
          return
        self._back.next = node
        self._back = node
        self._size = self._size + 1

    def pop(self):

        if(self._size == 0):
          raise IndexError("The queue is empty")
        node = self._front
        self._front = self._front.next
        if(self._front is None):
          self._back = None
        self._size -= 1
        return node.data
    
    def front(self):
      if(self._size == 0):
        raise IndexError("The queue is empty")
      return self._front.data

    def back(self):
      if(self._size == 0):
        raise IndexError("The queue is empty")
      return self._back.data
    
    def empty(self):
      return self._size == 0

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size


    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self._front
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()