#Selection sort ascending order
# nums=[5,2,5,4,6,2,7,3,8,9]
# l=len(nums)
# def selectionSort(nums):
#     l=len(nums)
#     for i in range(l):
#         miniIndex=i
#         for j in range(1+i,l):
#             if nums[miniIndex]>nums[j]:
#                 miniIndex=j
#         nums[i],nums[miniIndex]=nums[miniIndex],nums[i]
#     print(nums)
# selectionSort(nums)


# Selection sort in descending order
nums=[5,2,5,4,6,2,7,3,8,9]
l=len(nums)
def selectionSort(nums):
    l=len(nums)
    for i in range(l):
        maxIndex=i
        for j in range(1+i,l):
            if nums[maxIndex]<nums[j]:
                maxIndex=j
        nums[i],nums[maxIndex]=nums[maxIndex],nums[i]
    print(nums)
selectionSort(nums)