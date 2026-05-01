# optimize  Middle of the Linked List
# TorToise and Hare approach # Two pointer


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MiddleFinder:
    def find_middle(self, head):
        # Initialize pointers
        slow = head
        fast = head

        # Traverse: fast moves 2x, slow moves 1x
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is the middle
        return slow

# --- Execution ---
# 1. Create the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# 2. Link them
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# 3. Use the logic class
finder = MiddleFinder()
middle_node = finder.find_middle(node1)

print(f"The middle node value is: {middle_node.val}")
