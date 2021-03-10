from List import LinkedList

listt = LinkedList()

#Insert elements
listt.append(1)
listt.append(3)
listt.append("a")
listt.append(True)

#Print list
print(listt)

#Print list size
print(listt.__len__())

#Get node by index
print(listt.__getitem__(3))

#Set item by index
listt.__setitem__(3, "watermelon")

#Print list again
print(listt)

#Get fist index by value
print(listt.index("watermelon"))

#Insert element with index specified
listt.insert(2, "apple")

#Print list again
print(listt)

#remove node(s) by value
listt.remove("a")

#Print list again
print(listt)
