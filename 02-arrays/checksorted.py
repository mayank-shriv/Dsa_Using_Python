nums = [10,20,30,40,50,60]
l = len(nums) 
def checkSorted(nums):
    for i in range(0,l-1):
        if nums[i]>nums[i+1]:
            return False
    return True

print(checkSorted(nums))    