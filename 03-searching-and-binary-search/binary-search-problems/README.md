# Binary Search Problems

This folder is for interview-style binary search variations.

## Files

- `ceilAndFloor.py`
- `firstAndLastOccurence.py`
- `rotatedSortedArray.py`
- `searchInRotatedSortedArray.py`
- `timeofOccurence.py`

## Interview Tips

- First occurrence: when found, store answer and move left.
- Last occurrence: when found, store answer and move right.
- Count occurrence: last index minus first index plus one.
- Ceil is smallest value greater than or equal to target.
- Floor is largest value less than or equal to target.

## Hidden Traps

- In rotated arrays, duplicates can make the sorted-half check ambiguous.
- If target is absent, return `-1` or a clear sentinel consistently.
- An empty implementation file is a signal to revisit and complete it.
