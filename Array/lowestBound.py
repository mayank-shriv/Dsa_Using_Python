nums = [00,0,00,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,4,5,6,7,8,9,9,9,9,9]

target = 1
n = len(nums)
high = n-1
low = 0
lowerBound = -1
def lowerBound(nums,low,high, target):
    while(low<high):
        mid = (low+high)//2

        if nums[mid]>= target:
            lowerBound = mid
            high = mid-1
        else: 
            low = mid+1
    
    return lowerBound

print(lowerBound(nums,low, high, target))