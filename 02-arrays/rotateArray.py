
# # dont use slicing
# n = len(nums)
# temp = nums[-1]  # Store the last element
# for i in range(n - 1, 0, -1):
#     nums[i] = nums[i - 1]  # Shift elements to the right
# nums[0] = temp  # Place the last element at the beginning
# print(nums)

nums = [1,2,3,4,5,6]
n= len(nums)
k=int(input("Enter the kth position:"))
temp = []

for i in range(n-k,n):
    temp.append(nums[i])
    
temps = temp + nums[0:n-k]
print(temps)