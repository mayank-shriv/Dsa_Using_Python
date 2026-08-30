# Tree DFS

DFS is the backbone of tree interview problems.

## Files

- `preOrderbinaryTreeTraversal.py`
- `inOrderTreeTraversal.py`
- `binaryTreeTraversal_PostO.py`

## Interview Tips

- Preorder: node, left, right. Useful for copying or serializing.
- Inorder: left, node, right. For BST, it gives sorted order.
- Postorder: left, right, node. Useful when child results are needed first.

## Hidden Traps

- Traversal order matters. Say the order before writing code.
- For BST problems, inorder traversal is often the hidden trick.
