nums=[1,23,45,365465,768,787,98,9,56,4,36,26,164565,7687,464]
# method 1
# largest=0
# for i in nums:
#     if i>largest:
#         largest=i
# print(largest)

# method 2
largest =float("-inf")
n=len(nums)
for i in range (0,n):
    largest = max(largest,nums[i])
print(largest)