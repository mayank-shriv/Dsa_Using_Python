# Basic Search

Use this folder to revise the mechanics before harder binary search problems.

## Files

- `linearSearch.py`
- `binarySearch.py`

## Interview Tips

- Linear search is acceptable for small input or unsorted input.
- Binary search requires a sorted or monotonic search space.
- Clearly explain why half the search space can be removed.

## Hidden Traps

- Check inclusive versus exclusive bounds before writing the loop.
- For `while left <= right`, both `left = mid + 1` and `right = mid - 1` are required.
