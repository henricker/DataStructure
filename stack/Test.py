from Stack import Stack
stack = Stack()

#Inser elements
stack.push(1)
stack.push(2)
stack.push('oi')
stack.push('1.2')
stack.push(True)
stack.push('a')

#Print elements
print(stack)

#Erase two elements
stack.pop()
stack.pop()

#Print stack again
print(stack)

#Show queue size
print(stack.__len__())

#Check if stack is empty
print(stack.empty())

#Erase remaining elements
stack.pop()
stack.pop()
stack.pop()
stack.pop()

#Check again if stack is empty
print(stack.empty())