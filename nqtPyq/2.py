n = int(input())
arr = [int(input()) for _ in range(n)]
result = []
count = 0
for i in range(n):
	if arr[i] != 0:
		result.append(arr[i])
	else:
		count+=1
result.extend([0]*count)
print(result)
	
			   