# DSA Revision Workspace

This repo is organized for interview revision and job prep. The folder order starts with Python basics, then warmup problems, core DSA patterns, linked lists, trees, LeetCode-style practice, and company-specific practice.

## Folder Map

| Order | Folder | Use it for |
|---|---|---|
| 00 | [00-python-basics](00-python-basics/README.md) | Python syntax, collections, strings, input validation |
| 01 | [01-warmup-problems](01-warmup-problems/README.md) | Easy math, recursion, arrays, strings |
| 02 | [02-arrays](02-arrays/README.md) | In-place array work, two sum, rotate, bounds |
| 03 | [03-searching-and-binary-search](03-searching-and-binary-search/README.md) | Linear search, binary search, rotated arrays, ceil/floor |
| 04 | [04-sorting](04-sorting/README.md) | Bubble, selection, merge, quick sort |
| 05 | [05-hashing](05-hashing/README.md) | Frequency maps and lookup tricks |
| 06 | [06-bit-manipulation](06-bit-manipulation/README.md) | XOR, bit checks, masks |
| 07 | [07-linked-list](07-linked-list/README.md) | Singly and doubly linked list patterns |
| 08 | [08-trees](08-trees/README.md) | Tree traversal, BFS, DFS, height |
| 09 | [09-oops](09-oops/README.md) | OOP basics for interviews |
| 10 | [10-leetcode-patterns](10-leetcode-patterns/README.md) | Common LeetCode patterns |
| 11 | [11-company-infosys](11-company-infosys/README.md) | Infosys/company style coding practice |

## Daily Revision Flow

1. Pick 3 to 5 problems from [REVISION_TRACKER.md](REVISION_TRACKER.md).
2. Try each one cold for 20 to 30 minutes.
3. If stuck, read only your own code first, then rewrite the solution without looking.
4. Add the mistake pattern in the tracker: wrong edge case, wrong loop boundary, wrong data structure, or wrong complexity.
5. Revisit using spaced repetition: same day, next day, day 3, day 7, day 14.

## Interview Rules

- Start with brute force, then improve. Interviewers want to hear your thinking.
- Say constraints out loud. Constraints usually reveal the expected pattern.
- For sorted input, think binary search, two pointers, or sliding window.
- For repeated lookup/counting, think hashmap or set.
- For linked lists, consider dummy node, fast/slow pointers, and prev/current/next.
- For trees, define what your recursive function returns before coding.
- Always test empty input, one item, duplicates, negative numbers, already sorted input, and all-same values.

## How To Add New Problems

1. Put the solution in the closest topic folder.
2. Add it to [REVISION_TRACKER.md](REVISION_TRACKER.md).
3. Copy [PROBLEM_NOTES_TEMPLATE.md](PROBLEM_NOTES_TEMPLATE.md) when a problem teaches a new pattern or you made a useful mistake.

## Suggestions For Job Prep

- Rename older vague files like `1.py` and `2.py` when you revisit them, using clear snake_case names.
- Keep one problem per file and add a short top comment with problem name, pattern, time complexity, and space complexity.
- After every 10 problems, do one timed 45-minute mixed revision session.
- Keep a "mistake bank" in the tracker. Your repeated mistakes are the fastest path to improvement.
