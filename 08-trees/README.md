# 08 - Trees

Trees reward clean recursion. Before coding, define the meaning of the current node result.

## Subfolders And Files

- [BFS](BFS/README.md)
- [DFS](DFS/README.md)
- `binaryTree.py`
- `maximumHeightBt.py`

## Interview Tips

- DFS is natural for depth, path, subtree, and recursion-return problems.
- BFS is natural for level order, shortest path in unweighted trees, and per-level calculations.
- Height is usually `1 + max(left_height, right_height)`.
- Empty tree should usually return `0`, `None`, or `[]` depending on the question.

## Hidden Traps

- Be clear whether height counts nodes or edges.
- Recursive functions should return one clean meaning, not many half-related values.
- Queue-based BFS needs level size if the output is grouped by level.
