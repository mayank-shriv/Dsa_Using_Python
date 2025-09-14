nums = [6, 7, 4, 9, 2, 3, 8]

def partition(nums, low, high):
    pivot = nums[low]
    i, j = low, high
    while i < j:
        while i <= high and nums[i] <= pivot:
            
            i += 1
            
        while j >= low and nums[j] > pivot:
            
            j -= 1
            
        if i < j:
            
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[low], nums[j] = nums[j], nums[low]
    
    return j

def quicksort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1
    if low < high:
        p_index = partition(nums, low, high)
        quicksort(nums, low, p_index - 1)
        quicksort(nums, p_index + 1, high)
    return nums

print(quicksort(nums))
