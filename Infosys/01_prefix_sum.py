# A logistics company records the daily profit earned over N days.

# Some days have negative profit because of transportation costs.

# Your task is to answer Q queries.

# Each query contains two integers L and R.

# For every query, print the total profit earned from day L to day R.

# Input
# N = 8

# profits =

# 3 5 -2 7 1 -4 9 6

# Q = 4

# Queries

# 0 3
# 2 6
# 1 5
# 4 
# brute force approach  In this case time complexity is O(n*q) and space O(1)


arr = list(map(int, input().split()))
q = int(input())
ar1 = []
for _ in range(q):
    row = list(map(int, input().split()))
    ar1.append(row)

for q1 in ar1:
    sumValues = 0 
    a,b = q1
    while(a<=b):
        sumValues = arr[a]+ sumValues
        a+=1
    print(sumValues)



# optimal

# prefix sum  
arr = list(map(int, input().split()))
q = int(input())
ar1 = []
for _ in range(q):
    row = list(map(int, input().split()))
    ar1.append(row)

n = len(arr)
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

for q1 in ar1:
    a, b = q1
    print(prefix[b + 1] - prefix[a])