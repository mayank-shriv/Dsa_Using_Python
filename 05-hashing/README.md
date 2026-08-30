# 05 - Hashing

Hashing is your shortcut for fast lookup, counting, grouping, and duplicate detection.

## Files

- `hashing.py`

## Interview Tips

- Use a dict for frequencies, indexes, prefix sums, and grouping.
- Use a set when you only need existence.
- For two sum, store seen values and ask whether complement already exists.
- For anagrams, frequency count is clearer than sorting when you need O(n).

## Hidden Traps

- Average O(1) does not mean ordered.
- If duplicates matter, set may lose needed information.
- When storing indexes, decide whether first index or latest index is required.
