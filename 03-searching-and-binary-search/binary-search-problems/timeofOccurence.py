nums = [1,2,3,3,3,3,3,5,6,8,9,10]
target =3
def lowerBound(nums, target):
    low = 0
    n = len(nums)
    high = n-1
    lb = -1
    while(low<=high):
        mid = (low+high)//2
        if target <= nums[mid]:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb

def upperBound(nums, target):
    if lowerb ==-1:
        return -1
    low = 0
    n = len(nums)
    high = n-1
    ub = -1
    while(low<=high):
        mid = (low+high)//2
        if target < nums[mid]:
            ub = mid
            high = mid-1
        else:
            low = mid+1
        
    return ub


lowerb = lowerBound(nums, target)
ub = upperBound(nums, target)

print("time num occurs", ub-lowerb)