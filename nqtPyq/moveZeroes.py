n = int(input())
# arr = [int(input()) for _ in range(n)] # list comprehension
# result = []
# count = 0
# for i in range(n):
# 	if arr[i] != 0:
# 		result.append(arr[i])
# 	else:
# 		count+=1
# result.extend([0]*count)
# print(result)
	
 
# In-place two-pointer approach: O(n) time, O(1) extra space
 
arr = [int(input()) for _ in range(n)] # List comprehension
p = 0
for q in range(n):
    if arr[q] != 0:
        arr[p] = arr[q]
        p+=1

for i in range(p,n):
    arr[p] = 0

print(f'After moving all zeroes at the end list is looking like this {arr}')