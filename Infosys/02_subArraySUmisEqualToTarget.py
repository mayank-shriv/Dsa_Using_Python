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
    prefix_sum += num                     # [1,2,3,5 4] target = 7  
                                            
    if (prefix_sum - target) in seen:      # seen = {0, 1,3,6,11,15} Here there is no continuous sub string
        found = True
        break
    seen.add(prefix_sum)

print(found)



# [5,6,3,4] target = 7
seen = {0,5,11,14, 18}  
# prefix- target in seen        we can easily see 18 - 7 = 11 so 11 eleven in seen set 


    