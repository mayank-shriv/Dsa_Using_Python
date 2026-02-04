# optimal soln
nums = [1,1,1,-1,3,-3,0,0,0,2,2,-2]
nums.sort()
target = 3
n = len(nums)

result = []
for i in range(0,n-3):
    if i!=0 and nums[i]== nums[i-1]:
            continue
    for j in range (i+1, n-2):
        
        if j!=0 and nums[j]== nums[j-1]:
            continue
        k = j+1
        l = n-1

        while(k<l):
            total = nums[i]+nums[j]+ nums[k]+ nums[l]
            if total == target:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                result.append(temp)
                k+=1
                l-=1

                while k<l and nums[k] == nums[k-1]:
                    k+=1
            
                while k<l and nums[l]  == nums[l+1]:
                    l-=1
            if total>0:
                l-=1
            else :
                k+=1

print(result)