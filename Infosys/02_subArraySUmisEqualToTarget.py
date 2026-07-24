# Problem 2 (Infosys Style)

# You are given an integer array.

# Find whether there exists a continuous subarray whose sum equals K.

# Return True or False.

# Example

# Input

# [4,2,7,1,9,5]

# K = 10

# Output

# True
# Subarray Sum Equals K
# We can also solve this question with prefix_sum
arr = input().strip("[]")
arr = list(map(int, arr.split(',')))
target = int(input())

prefix_sum = 0
seen = {0}

found = False
for num in arr:
    prefix_sum += num
    if (prefix_sum - target) in seen:
        found = True
        break
    seen.add(prefix_sum)

print(found)



    