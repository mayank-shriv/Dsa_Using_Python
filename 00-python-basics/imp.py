arr = [1,2,3,4,5,6,7,8,9,10]
print(len(arr))  
print(min(arr))
print(max(arr))
print(sum(arr))
# abs(-10) 10
print(abs(-10))
# enumerate(arr)
#for i, num in enumerate(arr):
#range(10,0,-1) reverse loop

# List Comprehension
# squares = [x*x for x in arr]
# even = [x for x in arr if x%2==0]

#swap 
# a,b = b,a


#  Collections Module
from collections import Counter

# Frequency counting.

# Counter(arr)
p = Counter(arr)
print(p)
print(p.get(1,0))