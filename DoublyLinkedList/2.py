# Doubly Linked List
class Node:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next  = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
    
    #Insert at end
    def insert_at_end(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head
            while(currentNode.next):
                currentNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode

    def traversal(self):
        if self.head is None:
            print('There is no element in this doubly linked list')
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.val, end=" ")
            currentNode = currentNode.next
        print()

    # Insert at beginning(Head)
    def insert_at_head(self,val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    # Insert at between let's assume at 3
    def insert_at_pos(self,val,pos):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            currentNode = self.head
            if pos==1:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                return 

            i=2

            while(i<pos and currentNode.next):
                currentNode=currentNode.next
                i+=1
            
            if (currentNode.next is None):
                currentNode.next  = newNode
                newNode.prev = currentNode
                return
            
            previousNode = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode
            newNode.next = previousNode
    
    def delete_at_specific(self,pos):
        
        if not self.head:
            print(f'There is no doubly linked list')
        elif pos == 1:
            if currentNode.next:
                self.head = currentNode.next
                currentNode.next.prev = None    
                return
            else:
                self.head = None
                return 
        count = 0
        currentNode = self.head
        while(count<(pos-1) and currentNode):
            previousNode=currentNode
            currentNode = currentNode.next
            count+=1
        node = currentNode
        if not node:
            print("Out of Bound")
            return

        if node.next is None :
            previousNode.next = None
            return            
        previousNode.next = node.next
        node.next.prev = previousNode
        node.next = None
        

obj = doublyLinkedList()
obj.insert_at_head(30)
obj.insert_at_head(20)
obj.insert_at_head(10)
# obj.insert_at_pos(11,2)

# obj.insert_at_pos(12,3)

# obj.insert_at_pos(13,4)
# obj.insert_at_pos(31,7)
obj.delete_at_specific(5)

obj.traversal()





                
