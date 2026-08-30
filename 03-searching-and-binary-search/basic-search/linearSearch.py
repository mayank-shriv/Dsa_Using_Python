Nums= [1,2,4,34,543,242,454,24,3]
Target = 12
def findIndexOfTarget(nums,target):
    l = len(nums)
    for i in range(0,l):
        if nums[i]==target:
            return i
    return -1

print(findIndexOfTarget(Nums,Target))