# Iterative method 
nums = [1,2,3,4,5,6,7,8,9,10]
target = 13
n = len(nums)
low = 0
high = n - 1
found = False
while(low<=high):
    mid = (low+high)//2
    if nums[mid]== target:
        print(target, "is index at", mid)
        found = True
        break
    elif nums[mid]<target:
        low = mid+1
    
    else:
        high = mid-1

if found is False:
    print(target, "is not in the list")








# Recursive Method 
# nums = [1,2,3,4,5,6,7,8,9,10]
# target = 8
# n = len(nums)
# low = 0
# high = n - 1

# def BinarySearch(nums, low, high, target):
#     if low > high:
#         return -1
    
#     mid = (low + high) // 2
    
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] > target:
#         return BinarySearch(nums, low, mid - 1, target)
#     else:
#         return BinarySearch(nums, mid + 1, high, target)

# print("Index",BinarySearch(nums, low, high, target))
