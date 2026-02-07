nums = [1,1,1,-1,3,-3,0,0,0,2,2,-2]
"""
This script contains implementations of the "3Sum" problem, which finds all unique triplets in an array
that sum up to zero. The code includes three approaches: optimal, better, and brute force.
Key Points:
1. The optimal solution sorts the array and uses a two-pointer technique to reduce time complexity.
2. The condition `i != 0` ensures that duplicate triplets are avoided by skipping over repeated elements
    in the sorted array. This is because if `nums[i] == nums[i-1]` and `i != 0`, the triplet starting with
    `nums[i]` would already have been considered in a previous iteration.
3. The `better` solution uses a hash set to reduce the time complexity to O(n^2) by avoiding the innermost loop.
4. The brute force solution uses three nested loops to find all triplets, resulting in a time complexity of O(n^3).
Functions:
- Optimal solution: Uses sorting and two-pointer technique to find unique triplets.
- Better solution: Uses a hash set to optimize the search for the third element in the triplet.
- Brute force solution: Checks all possible triplets and stores unique ones in a set.
Usage:
- Replace the `nums` array with your input array to test the solutions.
"""


# optimal reducing space complecity

nums.sort() # O(nlogn)
# nums = [-3,-2,-1,0,0,0,1,1,1,2,2,3]
n = len(nums) # length of nums array
result = []
for i in range(0,n-2):
    if i!=0 and nums[i] == nums[i-1]:
        continue
    
    # moving to two pointers
    j= i+1
    k= n-1

    while(j<k):
        
        if nums[j]+nums[k]+nums[i] > 0 :
            k-=1
        elif nums[j]+nums[k]+nums[i]<0:
            j+=1
        else:
            temp = [nums[i], nums[j], nums[k]]
            result.append(temp)
            j+=1
            k-=1

            # skip the duplicate if occurs
            while j<k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]== nums[k+1]:
                k-=1

print(result)
        











# # better
# # arr[i]+ arr[j]+ arr[k] == 0
# # arr[k] == -(arr[i]+arr[j]) # this way we are reducing one loop and time T(C) = O(n**2) 
# nums = [1,2,3,-2,-1,0,4,-4,9,-9,8,-8]
# n = len(nums)
# result = set()

# for i in range(0,n):
#     mySet = set()
#     for j in range(i+1,n):

#         third = -(nums[i]+nums[j])
#         if third in mySet:
#             temp = [nums[i],nums[j], third]
#             temp.sort()
#             result.add(tuple(temp))
        
#         mySet.add(nums[j])

# [print(list(num),end=" ") for num in result]

# # brute force
# # n = len(nums)
# # myset = set()
# # for i in range(n):
# #     for j in range(i+1,n):
# #         for k in range(j+1,n):
# #             if nums[i]+nums[j]+nums[k] == 0:
# #                 ram = sorted([nums[i], nums[j], nums[k]])
# #                 
# #             myset.add(tuple(ram))
# # print(myset)