# Tree BFS

BFS processes the tree level by level.

## Files

- `(bfs)levelOrderTraversal.py`

## Interview Tips

- Use a queue.
- For level order output, capture `level_size = len(queue)` before the inner loop.
- Add children only after checking they are not `None`.

## Hidden Traps

- Without level size, all nodes may merge into one flat traversal.
- Do not use Python list `pop(0)` for large queues; use `collections.deque`.
