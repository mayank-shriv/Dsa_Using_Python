nums = [1,4,5,6,23,87,88,99,24,25,64,1,1]

mySet = set(nums)
longestCount = 0

for num in mySet:
    # check if num is the start of a sequence
    if (num - 1) not in mySet:
        current = num
        count = 1

        while current + 1 in mySet:
            current += 1
            count += 1

        longestCount = max(longestCount, count)

print(longestCount)

# brute force
# nums = [1,4,5,6,23,87,88,99,24,25,64]
# def longestSequence(nums):
#     l = len(nums)
 
#     maxCount = 0
#     for i in range(l):
#         ram = nums[i]
#         count = 1
#         for j in range(i+1,l):
            
#             if ram+1 == nums[j]:
#                 ram+=1
#                 count+=1
#         maxCount = max(count,maxCount)
       
#     print(maxCount)

# longestSequence(nums)


