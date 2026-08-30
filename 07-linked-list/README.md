# 07 - Linked List

Linked list interviews test pointer discipline. Draw nodes before coding and update links in a deliberate order.

## Subfolders

- [singly-linked-list](singly-linked-list/README.md)
- [doubly-linked-list](doubly-linked-list/README.md)

## Interview Tips

- Dummy nodes simplify insert/delete at head.
- Fast and slow pointers solve middle node, cycle detection, and loop length.
- Reverse needs three pointers: `prev`, `curr`, `next_node`.
- For deletion, think about which node owns the link you must change.

## Hidden Traps

- Losing `next` before changing `curr.next` breaks the list.
- Head changes must be returned from the function.
- Cycle problems require pointer identity, not node value equality.
