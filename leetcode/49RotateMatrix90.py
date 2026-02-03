# optimal soln
matrix = [[1,2,3],[4,5,6],[7,8,9]]
len_row, len_col = len(matrix),len(matrix[0])
    
for i in range(len_row):
    for j in range(i+1,len_col):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for i in range(len_row):
    matrix[i].reverse()



# # i did a mistake i was priting 90 degree rotated matrix but i have to make change in my original matrix
# # brute force approach
for i in range(len_row):
    for j in range(len_col):
        print(matrix[i][j], end=' ')
    print()
    
# for i in range(len_row):
#     for j in range(len_col-1,-1,-1):
#         print(matrix[j][i], end=" ")
#     print()