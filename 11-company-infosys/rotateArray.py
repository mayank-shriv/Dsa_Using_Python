arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
rotateAtPos = int(input("Enter the position to rotate the array by: "))
result1 = []
result = []
for i in range(rotateAtPos+1, len(arr)):
    result1.append(arr[i])
for p in range(rotateAtPos+1):
    result.append(arr[p])

ram = result1 + result
print("Rotated array:", ram)


n = len(arr)
step = (rotateAtPos + 1) % n
print("Step:", step)
rotated = arr[step:] + arr[:step]
print("Rotated array using slicing:", rotated)