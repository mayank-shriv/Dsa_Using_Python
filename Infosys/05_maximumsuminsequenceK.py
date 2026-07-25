# Problem 5
# A company monitors network traffic.
# Find the maximum sum of any K consecutive packets.
# 2 5 1 8 2 9 1
# K = 3
# Brute force

arr = list(map(int, input().split()))
k = int(input())
maxSum = 0
sum = 0
for i in range(len(arr)):
    if i < (len(arr)-k)+1:
        p = 0
        sum = 0
        while(p<k):
            sum = sum + arr[i]
            i+=1
            p+=1
        maxSum = max(maxSum,sum)
print(maxSum)

# Here the time complexity O(n2)


# Optimal soln will be sliding window 

arr = list(map(int, input().split()))
k = int(input())

window_sum = sum(arr[:k])   # sum of first window
maxSum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]   # add new element, remove old one
    maxSum = max(maxSum, window_sum)

print(maxSum)