# Problem 1 — Interview Mode

# Given an array of integers:

# nums = [2, 1, 5, 6, 2, 3]

# For every element, find the first element to its right that is greater than it.

# If no greater element exists, return -1.

# Example output
# [5, 5, 6, -1, 3, -1]


#Brute Force
# nums = [2, 1, 5, 6, 2, 3]
# ArrNums = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[j]>nums[i]:
#             ArrNums.append(nums[j])
#             break
#     else:
#         ArrNums.append(-1)

# print(ArrNums)


# optimal soln

nums = [2, 1, 5, 6, 2, 3]
retArr = [-1]*(len(nums))
# Output: [5, 5, 6, -1, 3, -1]
stack = []
for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        popped_index = stack.pop()
        retArr[popped_index] = nums[i]

    stack.append(i)


print(retArr)


