nums = [2,3,4,4,5,6,7,8,9]
target = 5
n = len(nums)
low = 0
high = n-1
ceil = -1 
floor = -1

while(low<=high):
    mid = (low+high)//2

    if nums[mid] == target:
        print("index is:", mid, "value is :", nums[mid])
        floor = nums[mid]
        ceil = nums[mid]
        break
    elif nums[mid]> target:
        ciel = nums[mid]
        high = mid-1
        
        

    else:
        floor = nums[mid]
        low = mid+1
print("floor is ", floor)
print("ceil is ", ceil)
        

    

