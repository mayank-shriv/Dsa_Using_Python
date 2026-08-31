# Next Problem — New Pattern
# Given an array:
# nums = [73, 74, 75, 71, 69, 72, 76, 73]
# For every day, find how many days you have to wait until a warmer temperature.
# If there is no warmer future temperature, return 0.
# Expected output:
# [1, 1, 4, 2, 1, 1, 0, 0]


# # Brute force approach
# nums = [73, 74, 75, 71, 69, 72, 76, 73]
# newArr = [0]*(len(nums))
# for i in range(len(nums)):
#     count = 0
#     for j in range(i+1, len(nums)):
#         count+=1
#         if nums[j]>nums[i]:
#             newArr[i] = count
#             break

# print(newArr)

# Space complexity  O(n^2) Because we are using an array of n size
# Time complexity O(n) Because we are using nested for loop



# Optimal Soln


nums = [73, 74, 75, 71, 69, 72, 76, 73]
# Expected output:
# [1, 1, 4, 2, 1, 1, 0, 0]
stack = []
newArr = [0]*len(nums)

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        index = stack.pop()
        pop_index = i - index   #Index value
        newArr[index] = pop_index

    stack.append(i)


print(newArr)

