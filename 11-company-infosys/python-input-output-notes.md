# Python Notes — sys, map, join (Infosys Exam Prep)

## 1. `sys`

Used for input/output at system level. Must import first:
```python
import sys
```

**Reading input:**
```python
line = sys.stdin.readline().strip()      # one line
lines = sys.stdin.readlines()            # all lines as list
data = sys.stdin.read().split()          # all input as list of tokens
```

**Other uses:**
```python
sys.exit()                    # stop program
sys.setrecursionlimit(10000)  # increase recursion limit
sys.maxsize                   # largest int value (use as "infinity")
```

**Example — read all numbers at once:**
```python
import sys
data = list(map(int, sys.stdin.read().split()))
```

---

## 2. `map()`

Applies a function to every element of an iterable. Returns a **map object** — must convert to `list()` to see/use values.

**Syntax:**
```python
map(function, iterable)
```

**Examples:**
```python
arr = list(map(int, input().split()))
# Input: 1 2 3 4  -> Output: [1, 2, 3, 4]

a, b, c = map(int, input().split())
# Input: 5 10 15  -> a=5, b=10, c=15

nums = [1, 2, 3]
strs = list(map(str, nums))
# Output: ['1', '2', '3']

squares = list(map(lambda x: x*x, [1,2,3,4]))
# Output: [1, 4, 9, 16]
```

⚠️ **Map object is exhausted after one use:**
```python
result = map(int, ['1','2','3'])
print(list(result))   # [1, 2, 3]
print(list(result))   # []  <- empty second time
```

---

## 3. `join()`

Combines list elements into a single string, with separator placed **before** the dot.

**Syntax:**
```python
separator.join(iterable)
```

**Examples:**
```python
' '.join(['Hello', 'World'])      # "Hello World"
','.join(['a', 'b', 'c'])         # "a,b,c"
''.join(['P','y','t','h','o','n'])# "Python"
```

⚠️ **Only works on strings** — convert numbers first:
```python
arr = [1, 2, 3]
','.join(map(str, arr))    # "1,2,3"   (correct)
','.join(arr)              # TypeError (wrong — arr has ints)
```

**Common output patterns:**
```python
print(*arr)                          # space separated: 1 2 3
print(' '.join(map(str, arr)))       # space separated: 1 2 3
print(','.join(map(str, arr)))       # comma separated: 1,2,3
```

---

## Quick Reference Table

| Task | Code |
|---|---|
| Read one int | `int(input())` |
| Read array (space-sep) | `list(map(int, input().split()))` |
| Read array (comma-sep) | `list(map(int, input().split(',')))` |
| Read all input fast | `sys.stdin.read().split()` |
| Print array space-separated | `print(*arr)` |
| Print array comma-separated | `','.join(map(str, arr))` |
