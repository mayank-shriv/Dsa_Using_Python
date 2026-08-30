nums = [1,2,3,3,3,3,3,5,6,8,9,10]

low = 0

target = 3
n = len(nums)
high = n-1
def lowerBound(nums,low, high, target):
    lb =-1
    check = 0
    while(low<=high):
        
        print("checkerLb", check+1)
        mid = (low+high)//2
        if target <= nums[mid]:
            lb = mid
            high = mid-1
        else:
            low = mid+1
    return lb


def UpperBound(nums,low, high, target):
    ub =-1
    if lb == -1:
        return -1
    check = 0
    while(low<= high):
        
        print("checker", check+1)
        mid = (low+high)//2
        if target < nums[mid]:                          
            ub = mid
            high = mid-1
        else:
            low = mid+1
    return ub
lb = lowerBound(nums,low, high,target)
ub = UpperBound(nums,low, high, target)
print("Upper Bound is: ", ub-1)
print("Lower Bound is: ", lb)
