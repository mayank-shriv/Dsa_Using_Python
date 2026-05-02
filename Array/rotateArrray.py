nums = [5, -2, 3, 9, 10, 34, 342]
# dont use slicing
n = len(nums)
temp = nums[-1]  # Store the last element
for i in range(n - 1, 0, -1):
    nums[i] = nums[i - 1]  # Shift elements to the right
nums[0] = temp  # Place the last element at the beginning