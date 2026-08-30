# Doubly Linked List

Doubly linked lists need both `next` and `prev` maintained.

## Files

- `1.py`
- `2.py`

## Interview Tips

- Every insert usually changes four links.
- Every delete must reconnect both neighbors.
- Head and tail cases should be handled explicitly or with sentinel nodes.

## Hidden Traps

- Updating `next` but forgetting `prev` creates a broken backward chain.
- Single-node list is both head and tail.
