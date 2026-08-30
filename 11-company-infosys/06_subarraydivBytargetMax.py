# Warehouse Shipment Analysis

# A warehouse records the weight of every package shipped each day.

# The manager wants to know the length of the longest continuous shipment period such that the total weight is divisible by K.

# Return only the maximum length.

# If no such subarray exists, print 0.
# input case
# 6

# 2 7 6 1 4 5

# 3 target

arr_input = list(map(int, input().split()))
target = int(input())
remainder_seen = {0: -1}
prefix_sum = 0
maxSubarray = 0
start = -1
for i in range(len(arr_input)):
    prefix_sum += arr_input[i]
    remainder = prefix_sum % target
    if remainder in remainder_seen:
        current_len = i - remainder_seen[remainder]

        if current_len > maxSubarray:
            maxSubarray = current_len
            start = remainder_seen[remainder] + 1

    else:
        remainder_seen[remainder] = i

print(maxSubarray)

if start != -1:
    print(arr_input[start:start + maxSubarray])


