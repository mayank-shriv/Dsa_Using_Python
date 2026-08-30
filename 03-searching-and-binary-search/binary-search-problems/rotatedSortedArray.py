nums = [15,16,1,2,3,4]
target =  16


def findIndex(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

print(findIndex(nums, target))



# # t(c) = logn
# def findTheNumberIndex(nums, target, low, high):
#     while (low<=high):
#         mid = (low+high)//2                     
#         if nums[mid] == target:
#             return mid
#         elif nums[mid]<target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1


# print(findTheNumberIndex(nums, target, low, high))
