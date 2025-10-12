nums = [1,2,3,4,0,7,5,0,0,7]
def moveZeroAtEnd(nums):
    n = len(nums)
    i,j=0,1
    if len(nums)==1:
        return
    while(i<n):
        if j==n:
            break
        
        if nums[i]!=0:
            i+=1
            j+=1
        if nums[i]==0:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
            
        
    return nums

print(moveZeroAtEnd(nums))    
