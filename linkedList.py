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
   

n1 = Node(21)
print(n1) # node is stored at <__main__.Node object at 0x000001CC67A18B50>>
# print(n1.getData()) # 21
# print(n1.getNext()) # view next node

n2 = Node(10)
# print(n2)
n2.setNext(n1)
print(n2.getNext())

myList = linkedList()
print(myList.isEmpty())


