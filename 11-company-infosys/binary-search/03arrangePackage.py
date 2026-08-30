# Problem 3
# Capacity to Ship Packages Within D Days

# You are given an array where each element represents the weight of a package.

# weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# days = 5

# A ship transports packages in the given order.

# Rules:

# Packages cannot be reordered.
# All packages loaded on the same day must have a total weight less than or equal to the ship's capacity.
# Find the minimum ship capacity needed to deliver all packages within days.
# Example

# If the ship capacity is 15:

# Day 1: 1 + 2 + 3 + 4 + 5 = 15
# Day 2: 6 + 7 = 13
# Day 3: 8
# Day 4: 9
# Day 5: 10

# So capacity 15 works.

# weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# days = 5

weights = list(map(int, input().split()))
days = int(input())

def checkCapacity(capacity, weights,days):
    dayCount = 1
    prefixSum = 0
    for weight in weights:
        prefixSum += weight
        if prefixSum > capacity:
            dayCount+=1
            prefixSum = weight

    if dayCount > days:
        return False

    return True 

def shipCapacity(weights, days):
    low = max(weights)
    high = sum(weights)
    while(low<=high):
        capacity = (low + high)//2
        if  checkCapacity(capacity, weights, days):
            answer = capacity
            high = capacity -1
        else:
            low = capacity + 1

    return answer


print(shipCapacity(weights, days))
