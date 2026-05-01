# Linked List 
# Singly Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    


# node1 = Node(1)
# node2 = Node(2)
# node3= Node(3)
# node4 = Node(4)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = None



# print(node1)    # It will return obj address <__main__.Node object at 0x000002C331E37230>

# print(node1.val)
# print(node1.next) # It will return Node 2 obj's address
# print(node2)  # It will return Node 2 obj's address



# More Efficient Way: 

# We are creating Singly Linked List class

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def appendInSinglyLinkedList(self,val):  
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next

            currentNode.next = newNode   # It will insert at End



    def traversal(self):
        if self.head == None:
            return f'There is no element in this singly linked list'
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.val, end=" ")
                currentNode = currentNode.next


    def insertAtSpecificPosition(self, val, pos):
        newNode = Node(val)

        if self.head == None and pos > 0:
            return f'We can not insert this value at this position because It execeed the sll size'
        elif pos == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            currentNode = self.head
            previousNode =None
            for i in range(0,pos):
                previousNode = currentNode
                currentNode = currentNode.next

            previousNode.next = newNode
            newNode.next = currentNode


    def deleteAtSpecificPlace(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos < 0:
            print("Invalid position")
            return

    # Delete head
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return

        previousNode = None
        currentNode = self.head

        for i in range(pos):
            if currentNode is None:
                print("Position out of range")
                return
            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            print("Position out of range")
            return

        previousNode.next = currentNode.next
        currentNode.next = None

            


# ssl = singlyLinkedList()
# ssl.appendInSinglyLinkedList(12)
# ssl.appendInSinglyLinkedList(13)
# ssl.appendInSinglyLinkedList(14)
# ssl.traversal()
# ssl.deleteAtSpecificPlace(0)
# ssl.insertAtSpecificPosition(15,2)
# print(end="\n")
# ssl.traversal()

