class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext

class linkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0 
        while current != None:
            count += 1
            current = current.getNext()
        return count

n1 = Node(21)
print(n1) # node is stored at <__main__.Node object at 0x000001CC67A18B50>>
# print(n1.getData()) # 21
# print(n1.getNext()) # view next node

n2 = Node(10)
# print(n2)
n2.setNext(n1)
print(n2.getNext())

myList = linkedList()
# print(myList.isEmpty())

myList.add(99) # adding item to node
print(myList.isEmpty())
print(myList.head)

myList.add(93)
print(myList.head)
print(myList.head.data)

myList.add(97)
print(myList.size())
print(myList.head)
# print(myList.head.getNext())
print(myList.head.getNext().getNext())