array = [1, 2, 3, 4, 5, 6, 7]

def merge_sort(arr):
    # Base case: single element or empty array is already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Recursive call on left half
    right = merge_sort(arr[mid:])  # Recursive call on right half
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Test

# print(merge_sort(array) == array)  # True

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

print(quicksort(array)==array)
