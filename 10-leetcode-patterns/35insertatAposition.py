nums = [1,3,4,5]
target = 2
n = len(nums)
low = 0
high= n-1

while (low<=high):
    mid = (low+high)//2

    if nums[mid]>target:
        high = mid-1
    else:
        low = mid+1
    


  
    
print(low)







