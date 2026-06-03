class Node:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next  = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4
n5.prev = None


def traversal(n1):
    if n1 == None:
        return f'There is no element in this singly linked list'
    else:
        currentNode =  n1
        while currentNode is not None:
            print(currentNode.val, end=" ")
            currentNode = currentNode.next
                
traversal(n1)