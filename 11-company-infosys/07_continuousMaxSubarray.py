# Delivery Route Optimization
# A logistics company has N delivery centers arranged in a straight line.
# Each center has a certain number of packages.
# The company wants to ship packages in one continuous route.
# Find the maximum number of packages that can be collected in a continuous route such that the total number of packages is exactly K.
# If no such route exists, print 0.
# Input Format
# N
# p1 p2 p3 ... pN
# K
# Sample Input 1
# 8
# 1 2 3 1 1 1 2 3
# 6
# Sample Output 1
# 4
# Explanation
# One valid route is:
# 3 1 1 1
# Sum = 6
# Length = 4
# There are other subarrays with sum 6, but none is longer.

n = int(input())

arr = list(map(int, input().split()))

target = int(input())

prefix_sum = 0
seen = {0: -1}

maxLength = 0
start = -1

for i in range(n):

    prefix_sum += arr[i]

    required = prefix_sum - target

    if required in seen:

        currentLength = i - seen[required]

        if currentLength > maxLength:
            maxLength = currentLength
            start = seen[required] + 1

    if prefix_sum not in seen:
        seen[prefix_sum] = i

print(maxLength)

if start != -1:
    print(arr[start:start + maxLength])