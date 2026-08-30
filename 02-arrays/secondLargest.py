# Brute Force / Using Pre defined methods
def secondLargest(nums):
    nums.sort()
    return nums[-2]

nums = [10,20,30,40]
print(secondLargest(nums))

# Optimal Way 
def secondLargest(nums):
    largest = float("-inf")
    secondLarge = float("-inf")
    for i in nums:
        if i > largest:
            secondLarge = largest
            largest = i  
        elif i > secondLarge and i < largest:
            secondLarge = i 
    return secondLarge
print(secondLargest(nums))