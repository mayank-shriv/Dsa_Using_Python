# Optimal soln







# Brute Force
class SinglyLinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None

node1 = SinglyLinkedList(1)
node2 = SinglyLinkedList(2)
node3 = SinglyLinkedList(3)
node4 = SinglyLinkedList(4)
node5 = SinglyLinkedList(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# to solve this problem I am using stack data sructure 

def reverseTheString(node):
    head = node
    list = []
    while(head is not None):
        list.append(head.val)
        head = head.next
    head = node
    while(head is not None):
        head.val = list.pop()
        head = head.next

    return node

rLL = reverseTheString(node1)
values = []
curr = rLL
while curr:
    values.append(str(curr.val))  # Convert to string for .join()
    curr = curr.next

# 2. Now join the list of strings
print("->".join(values))