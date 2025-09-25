
from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)


one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

def levelOrder(one):
    result = []
    queue = deque([])
    queue.append(one)
    while len(queue) != 0:
        e = queue.popleft()
        result.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    
    return result

list = levelOrder(one)
print(list)
