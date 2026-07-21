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
arr = [int(input()) for _ in range(n)]
write = 0
for read in range(n):
	if arr[read] != 0:
		arr[write] = arr[read]
		write += 1

for i in range(write, n):
	arr[i] = 0

print(arr)