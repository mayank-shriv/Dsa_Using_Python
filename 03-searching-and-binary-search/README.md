# 03 - Searching And Binary Search

Binary search is not only for finding a number. It is also for finding the first valid answer in a monotonic decision space.

## Subfolders

- [basic-search](basic-search/README.md) - linear search and simple binary search
- [binary-search-problems](binary-search-problems/README.md) - bounds, occurrences, rotated arrays

## Interview Tips

- Before binary search, say what is monotonic.
- Decide whether your search space is indexes, values, or answer candidates.
- Keep the invariant clear: "left side is invalid, right side may be valid" or similar.
- Use `mid = left + (right - left) // 2` as a portable habit.

## Hidden Traps

- Infinite loops usually come from not moving `left` or `right`.
- Rotated sorted arrays need you to detect which half is sorted.
- For first and last occurrence, normal binary search is not enough; continue searching after a match.
