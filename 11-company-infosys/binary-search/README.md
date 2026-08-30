# Infosys Binary Search

These are binary-search-on-answer style problems. The trick is writing a helper that answers "can we do this with value X?"

## Files

- `01arrangeBook.py`
- `02aggresiveCow.py`
- `03arrangePackage.py`
- `04MinimumPreocessingSpeed.py`
- `output.py`

## Interview Tips

- Search the answer, not the array, when the question asks for minimum maximum, capacity, speed, distance, or days.
- Write `can(mid)` first in plain English.
- If `can(mid)` is true and you need minimum value, move right.
- If `can(mid)` is true and you need maximum value, move left.

## Hidden Traps

- Low and high bounds decide correctness. Use realistic bounds from the problem.
- Aggressive cows style problems usually maximize minimum distance.
- Book allocation style problems usually minimize maximum pages.
