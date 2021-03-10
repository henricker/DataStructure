from Queue import Queue

queue = Queue()

#Insert elements
queue.push(1)
queue.push(3)
queue.push("a")
queue.push(True)

#Get front data
print(queue.front())

#Get back data
print(queue.back())

#Check if is empty
print(queue.empty())

#Print queue
print(queue)

#Remove elements
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())


#Check again if queue is empty
print(queue.empty())