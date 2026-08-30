#Bubble sort
nums=[8,5,3,6,4,6,35,2,52]
def bubbleSort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j+1]<nums[j]:
                nums[j+1],nums[j]=nums[j],nums[j+1]
    print(nums)
bubbleSort(nums)