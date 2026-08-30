# 00 - Python Basics

Use this folder when Python syntax slows you down during problem solving. In interviews, Python basics matter because small mistakes in input, loops, slicing, and dictionaries can waste the whole round.

## Files

- `basic.py` - basic Python practice
- `array.py` - list and array-style operations
- `dict.py` - dictionary operations
- `set.py` - set operations
- `string.py` - string operations
- `imp.py` - important syntax notes
- `usernameValidation.py` - Python validation practice
- `uservalidation.js` - JavaScript validation practice

## Interview Tips

- Know when to use `list`, `set`, and `dict`: list preserves order, set removes duplicates, dict stores key-value counts or indexes.
- `in` on a list is O(n), but `in` on a set or dict is average O(1).
- Use `enumerate(arr)` when you need both index and value.
- Use `dict.get(key, 0)` for frequency counting.
- Be careful with slicing because it creates a new list or string.

## Hidden Traps

- Do not use a mutable default argument like `def solve(arr=[])`.
- `map()` returns an iterator, so convert it with `list()` if you need to reuse it.
- String operations often create new strings. For many joins, collect parts in a list and use `"".join(parts)`.
