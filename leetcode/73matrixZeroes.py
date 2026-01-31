
nums = [[1,0,3],[3,5,5],[6,5,56]]
r,c = len(nums), len(nums[0])
rowTrack,colTrack = [0]*r,[0]*c
for i in range(r):
    for j in range(c):
        if nums[i][j]==0:
            rowTrack[i]=-1
            colTrack[j]=-1
    
for i in range(r):
    for j in range(c):
        if (rowTrack[i] == -1) or (colTrack[j] == -1):
            nums[i][j] = 0
print(nums)




# brite force
# def findZero(nums):
   
#     for i in range(0,r):
#         for j in range(0,c):
#             if (nums[i][j]) == 0:
#                 setInfinitive(nums,i,j)
    
# def setInfinitive(nums,i,j):
#     for i1 in range(0,r):
#         if nums[i][i1]!=0:
#             nums[i][i1] = float("inf")
#     for i2 in range(0,c):
#         if nums[i2][j]!=0:
#             nums[i2][j]  = float("inf")

# def setZero(nums):
#     for i in range(r):
#         for j in range(c):
#             if nums[i][j] == float("inf"):
#                 nums[i][j] = 0
#     print(nums)
# findZero(nums)
# setZero(nums)



    
