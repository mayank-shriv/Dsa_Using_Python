#Brute Force 
list = [1,-3,4,5,4,6,7,-6,-76,-67,6,6,13,-23]
total = 0
maxSubArrayTotal = float("-inf")
l = len(list)
for i in range(0,l):
    for j in range(i,l):
        total = total+list[j]
        if maxSubArrayTotal < total:
            maxSubArrayTotal = total
    total = 0
print(maxSubArrayTotal)

#Optimal Solution (Kadan's algorithm)

nums = [1,3,34,45,494,645,483,-34,-34324]
maximum = float("-inf")
total = 0
l = len(nums)
for i in range(l):
    total = total + nums[i]
    maximum = max(total,maximum)
    if total<0:
        total = 0
print(maximum)
