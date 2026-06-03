from singlyLinkedList import node1, Node

ssl = node1

def lengthOfLoop(node):
    if node is None or node.next is None:
        return "There is no cycle"
    
    slow = node
    fast = node
    
    # 1. Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # 2. Cycle found! Now find the length.
            # Keep fast still and move slow until it hits fast again.
            count = 1
            slow = slow.next
            while slow != fast:
                count += 1
                slow = slow.next
            return count
            
    return "There is no cycle"

print(f"Length of the loop: {lengthOfLoop(ssl)}")