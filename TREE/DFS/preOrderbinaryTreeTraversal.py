# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None


# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)


# one.left = two
# one.right = three
# two.left = four
# two.right = seven
# three.left = six
# three.right = five



# def preOrderTraversal(root):
#     if root == None:
#         return
#     preOrderTraversal(root.left)
#     print(root.val,end=" ")
#     preOrderTraversal(root.right)


# preOrderTraversal(one)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_iterative(root):
    """Return pre-order traversal using an explicit stack."""
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def print_pre_order(root):
    values = pre_order_iterative(root)
    print(" -> ".join(map(str, values)))


# Build tree
root = Node(1,
            left=Node(2, Node(4), Node(7)),
            right=Node(3, Node(6), Node(5)))

print_pre_order(root)
