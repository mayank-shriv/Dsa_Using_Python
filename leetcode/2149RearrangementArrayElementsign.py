# optimal 
nums = [5,10,-3,-1,-10,6]
l = len(nums)
result = [0] * l
p,q= 0,1
for i in range(l):
    if nums[i]>=0:
        result[p]=nums[i]
        p+=2
    else:
        result[q]= nums[i]
        q+=2
    
    
print(result)

# # brute force 
# nums = [5,10,-3,-1,-10,6]
# plusN = []
# negN = []

# for num in nums:
#     if (num>0):
#         plusN.append(num)
#     if (num<0):
#         negN.append(num)
# l=3
# i=0
# ram = []
# while (i<l):
#     ram.append(plusN[i])
#     ram.append(negN[i])
#     i+=1
# print(ram)