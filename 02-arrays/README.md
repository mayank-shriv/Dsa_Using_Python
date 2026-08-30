# 02 - Arrays

Arrays are the highest-return topic for interviews. Revise this folder until you can quickly choose between brute force, hashing, two pointers, prefix sums, and binary search.

## Files

- `app.py`
- `checksorted.py`
- `highBound.py`
- `largestEle.py`
- `lowestBound.py`
- `moveZeroAtTheEndOfList.py`
- `removeDuplicate.py`
- `rotateArray.py`
- `rotateArrray.py`
- `secondLargest.py`
- `twoSum.py`

## Interview Tips

- If the array is sorted, first think two pointers or binary search.
- If the problem asks for pairs or previous values, think hashmap.
- If the problem asks for subarray sum, think prefix sum or sliding window.
- If asked to do it in-place, track write index separately from read index.
- For rotation, the reversal trick is usually clean: reverse whole array, then reverse parts.

## Hidden Traps

- Duplicates change the answer for two sum, remove duplicates, second largest, and bounds.
- Empty array and single-item array should be tested first.
- Lower bound means first index with value greater than or equal to target.
- Upper bound means first index with value greater than target.
