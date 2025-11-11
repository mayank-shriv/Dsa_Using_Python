# Brute force
nums = [12, 22, 3, 2223, 1, 223, 443, 2]
target = 5

def two_sum(nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i + 1, l):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

result = two_sum(nums, target)
print(result)