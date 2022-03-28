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
    def display(self):
        current = self.head
        array = []
        while current != None:
            print(current.data)
            array.append(current.data)
            current = current.getNext()
        return array
    def search(self, item):
        current = self.head
        find = False
        while current != None:
            if current.data == item:
                # return True but cann't return false value
                find = True
                break
            else:
                current = current.getNext()
        return find
    def remove(self, item):
        current = self.head
        if self.search(item):
            previous = None
            while current != None:
                if current.data == item:
                    if current.getNext() != None:
                        previous.setNext(current.getNext())
                        break
                else:
                    previous = current
                    current = current.getNext()
    # def remove(self, item):
    #     current = self.head
    #     previous = None
    #     found = False
    #     while not found:
    #         if current.getData() == item:
    #             found = True
    #         else:
    #             previous = current
    #             current = current.getNext()
    #         if previous == None:
    #             self.head = current.getNext()
    #         else:
    #             previous.setNext(current.getNext())

n1 = Node(21)
print(n1) # node is stored at <__main__.Node object at 0x000001CC67A18B50>>
# print(n1.getData()) # 21
# print(n1.getNext()) # view next node

n2 = Node(10)
# print(n2)
n2.setNext(n1)
print(n2.getNext())

#========= START LINKED LIST =========#
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
print(myList.display())
print(myList.search(93))
myList.add(66)
print(myList.display())
# print(myList.remove(93))
# print(myList.display())