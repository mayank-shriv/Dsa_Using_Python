# Problem 3 (Infosys Style)

# A company stores user login IDs.

# You are given a sorted list of IDs.

# Find two IDs whose sum equals X.

# 1 4 6 8 9 12 18

# Target = 20

# Return indices.


# Two sum problem 
arr = list(map(int, input().split()))
target = int(input())

left = 0
right = len(arr) - 1
found = False

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print(left, right)
        found = True
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No pair found")