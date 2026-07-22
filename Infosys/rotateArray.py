arr = [1, 2, 3, 4, 5, 6, 7]
rotateAtPos = 3
result1 = []
result = []
for i in range(rotateAtPos+1,len(arr)):
    result1.append(arr[i])
for p in range(rotateAtPos+1):
    result.append(arr[p])

ram = result1+result
print(ram)


n = len(arr)
step = (rotateAtPos + 1) % n
print(step)
rotated = arr[step:] + arr[:step]
print(rotated)