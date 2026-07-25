# Problem 3 (Infosys Style)

# A company stores user login IDs.

# You are given a sorted list of IDs.

# Find two IDs whose sum equals X.

# 1 4 6 8 9 12 18

# Target = 20

# Return indices.


# Two sum problem 


# Brute force

# arr = list(map(int,input().split())) # This way we will take space separated values in a list 
# target = int(input())
# Here we are taking matching value

# for i in range(len(arr)):
#     j = i+1
#     while (j<len(arr)):
#         if arr[i]+arr[j] == target:
#             print(*[i,j])
#         j+=1

# Optimal soln

arr = list(map(int, input().split()))
target = int(input())
seen = {}
for i in range(len(arr)):
    value = target - arr[i]
    if value in seen:
        print(seen[value],i)

    seen[arr[i]] = i
          

# arr = list(map(int, input().split()))
# target = int(input())

# left = 0
# right = len(arr) - 1
# found = False

# while left < right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == target:
#         print(left, right)
#         found = True
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1

# if not found:
#     print("No pair found")