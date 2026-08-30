from singlyLinkedList import singlyLinkedList
# Find the middle of the Linked List 

ssl = singlyLinkedList()
ssl.appendInSinglyLinkedList(12)
ssl.appendInSinglyLinkedList(13)
ssl.appendInSinglyLinkedList(14)
# ssl.traversal()
ssl.deleteAtSpecificPlace(0)
ssl.insertAtSpecificPosition(15,2)
print(end="\n")
# ssl.traversal()


count = 0
temp = ssl.head
while temp is not None:
    temp = temp.next
    count+=1
if count//2 == 0:
    n = ((count//2)+1)
else:
    n = ((count+1)//2)


# brute force
temp = ssl.head
for i in range(n-1):
    temp = temp.next

print(temp.val)

