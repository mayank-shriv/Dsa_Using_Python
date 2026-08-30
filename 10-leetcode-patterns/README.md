# 10 - LeetCode Patterns

This folder is for mixed pattern recognition. Use it after topic-wise revision so you can identify the approach from the problem statement.

## Files And Patterns

- `121bestTimeToBuyAStock.py` - one pass, running minimum
- `128longestSeqeunce.py` - hash set, sequence start
- `15ThreeSum.py` - sorting plus two pointers
- `18LeetCode_4sumProblem.py` - sorting plus k-sum
- `2149RearrangementArrayElementsign.py` - positive/negative placement
- `35insertatAposition.py` - binary search insertion point
- `49RotateMatrix90.py` - matrix transpose/reverse
- `54listspiralmatrixElement.py` - matrix boundaries
- `73matrixZeroes.py` - matrix marking
- `leetcode876.py` - linked list middle
- `maximumSubArraySum.py` - Kadane algorithm
- `reverseALinkedList.py` - linked list reversal

## Interview Tips

- For arrays with target sum, ask: sorted or unsorted?
- For maximum subarray, Kadane means "extend or restart".
- For matrix traversal, maintain boundaries and shrink after each direction.
- For linked list LeetCode problems, draw before coding.

## Hidden Traps

- Three sum must skip duplicate values after sorting.
- Matrix zeroes can require O(1) extra space using first row and first column as markers.
- Longest consecutive sequence starts only when `num - 1` is absent.
