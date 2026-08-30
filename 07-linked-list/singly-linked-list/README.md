# Singly Linked List

Use this folder for one-direction pointer problems.

## Files

- `singlyLinkedList.py`
- `findThelengthoftheLoop.py`
- `2.py`

## Interview Tips

- For reverse, save `next_node` before redirecting `curr.next`.
- For cycle length, first meet using fast/slow pointers, then walk once around the cycle.
- For middle node, move slow one step and fast two steps.

## Hidden Traps

- Returning old head after reversal is wrong; return `prev`.
- If fast or `fast.next` is `None`, there is no cycle.
