nums = [1,1,1,-1,3,-3,0,0,0,2,2,-2]


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