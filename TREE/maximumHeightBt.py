# In this file we are creating code to find maximum depth (height ) of Binary Tree

import math
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