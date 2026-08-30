# Problem 1 — Interview Mode

# Given an array of integers:

# nums = [2, 1, 5, 6, 2, 3]

# For every element, find the first element to its right that is greater than it.

# If no greater element exists, return -1.

# Example output
# [5, 5, 6, -1, 3, -1]


#Brute Force
nums = [2, 1, 5, 6, 2, 3]
ArrNums = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j]>nums[i]:
            ArrNums.append(nums[j])
            break
    else:
        ArrNums.append(-1)

print(ArrNums)


# optimal soln
class Solution:

    def nextGreaterElement(self, nums) :
        # Initialize the result array filled with -1
        arrRet = [-1] * len(nums)

        # This stack will store the indices (positions) of the numbers
        stack = []

        for i in range(len(nums)):
            # While stack is not empty and current number is greater than
            # the number corresponding to the index on top of the stack
            while stack and nums[i] > nums[stack[-1]]:
                # Pop the index from the stack
                popped_index = stack.pop()
                # The current number is the next greater element for the popped index
                arrRet[popped_index] = nums[i]

            # Push the current index onto the stack
            stack.append(i)

        return arrRet


# Testing the logic with your example
nums = [2, 1, 5, 6, 2, 3]
sol = Solution()
print(sol.nextGreaterElement(nums))
# Output: [5, 5, 6, -1, 3, -1]


