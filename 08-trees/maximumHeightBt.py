# In this file we are creating code to find maximum depth (height ) of Binary Tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
     

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

def maximumHeight(node):
    if node == None:
        return 0
    leftHeight = maximumHeight(node.left)
    rightHeight = maximumHeight(node.right)
    return 1+ max(leftHeight,rightHeight)
print(maximumHeight(node1))





# Iterative Method (Level Order)

from collections import deque
def level_order(root):
    queue = deque([])
    height = 0
    queue.append(root)
    while len(queue)!= 0:
        level_size = len(queue)
        height+=1
        for _ in range(level_size):
            e = queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height
print(level_order(node1))


# myWay
def levelOrder(node):
    queue = []
    height = 0
    queue.append(node)
    while  len(queue)!= 0:
        levelSize = len(queue)
        height += 1
        for _ in range(levelSize):
            e= queue[0]
            del queue[0]
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height
print(levelOrder(node1))