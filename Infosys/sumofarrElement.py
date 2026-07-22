# Sum of arrqay element 
# ele = 1
# n = int(input("How many elements in your array: "))
# n_arr = [int(input(f'Enter the {ele} Element: '))  for ele, _ in enumerate(range(n), start = 1) ]
# sum = 0
# for i in n_arr:
#     sum = sum + i

# print(f'Sum of array element is {sum}') 



# Find pair with given sum 
# Brute Force
# arr = [1,2,3,4,5,6,7,8,9]
# target = 9
# n = len(arr)
# result = []
# i, k = 0, 0
# while(i<n):
#     k = 0
#     while(k<n):
#         if arr[i]+arr[k] == target:
#             result.append((arr[i],arr[k]))
#         k+=1
#     i+=1   
# print(result)


# Optimal approach: Use a hash set to store seen elements.
# Time Complexity: O(n)
# Space Complexity: O(n)

seen = set()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
result = []

for num in arr:
    complement = target - num
    if complement in seen:
        result.append((num, complement))
    seen.add(num)

print(result)


