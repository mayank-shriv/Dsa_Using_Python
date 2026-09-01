# Stock Span Problem
# You have stock prices for consecutive days:
# Day:     0    1    2    3    4    5    6
# Price:  100  80   60   70   60   75   85
# For each day, we need to find its span.
# What does span mean?

# For today's price, count:

# How many consecutive days going backward (including today) had a price less than or equal to today's price?


# Brute Force approach

# nums = [100,80,60,70,60,75,85]
# result = []
# for i in range(len(nums)):
#     j = i-1
#     count = 1
#     while j>=0 and nums[i] > nums[j]:
#         count+=1
#         j-=1

#     result.append(count)
# print(result)


# Optimal Solution
nums = [100, 80, 60, 70, 60, 75, 85]
stack = []
newArr = []

for i in range(len(nums)):
    while stack and nums[stack[-1]] <= nums[i]:
        stack.pop()

    if not stack:
        span = i + 1
    else:
        span = i - stack[-1]

    newArr.append(span)
    stack.append(i)

print(newArr)
