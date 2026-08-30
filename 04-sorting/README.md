# 04 - Sorting

Sorting questions test fundamentals, but they also appear as helper steps inside bigger problems.

## Files

- `bubbleSort.py`
- `selectionSort.py`
- `MergeSort.py`
- `quickSort.py`

## Interview Tips

- Know time complexity without thinking: bubble and selection are O(n^2), merge and quick average O(n log n).
- Merge sort is stable and predictable, but uses extra space.
- Quick sort is usually fast, but bad pivot choice can become O(n^2).
- Sorting can simplify pair, interval, greedy, and duplicate problems.

## Hidden Traps

- Selection sort is not stable by default.
- Merge sort bugs often happen when copying leftover elements.
- Quick sort partition bugs usually come from equal elements and pointer crossing.
