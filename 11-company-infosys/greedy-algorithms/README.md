# Infosys Greedy Algorithms

Greedy works when a local best choice can safely build a global best answer.

## Files

- `01.meeting.py`

## Interview Tips

- For meeting problems, sort by end time.
- Explain the greedy choice in one sentence before coding.
- Keep the last selected end time and count compatible intervals.

## Hidden Traps

- Sorting by start time is usually wrong for maximum non-overlapping meetings.
- Check whether touching intervals are allowed, such as `start >= end`.
