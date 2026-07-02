# Reverse a arr (List)

arr = [1,2,3,4,5,6,7,8,9,10]
# here we are the using any slicing [::-1] or reverse()
newArr = []

for i in range(len(arr)-1,-1,-1):
    newArr.append(arr[i])

print(newArr) #here the time complexity is O(n) also space complexity is  O(n)

# optimal soln is we can also save our memory (space)
arr = [1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(arr)-1
while(left<right):
    arr[left],arr[right] = arr[right], arr[left]
    left,right = left+1, right-1

print(arr) # that way we solved the space problem also.
# Find the second highest in arr

# second highest with sorting
arr = [3,8,2,9,1]
maxNum = float("-inf")
secondMax = float("-inf")
for i in arr:
    if maxNum<i:
        secondMax = maxNum
        maxNum = i
    if secondMax<i and i<maxNum:
            secondMax = i
print(f'Second max is ', secondMax)
    

 #O(nlogn)
# print(f'second highest value in this array is:{arr[-2]}')
# T.C. O(nlogn) sorting part

# put all zeroes at last 

arr =[1,0,2,0,5]
n = len(arr)
# newArr = [0]*n #It will create an arr which holds n elements and all elements are zeroes.
# p = 0
# arr.sort()
# for i in range(n): #O(n)
#     if arr[i] != 0: #O(1)
#         newArr[p] = arr[i]
#         p+=1
# print(newArr) 

# optimal without creating a new arr
arr =[1,0,2,0,5,2,3,4,5,4,65,4,6,4,7,80,0,0,0,0,0,0,0,0,56,56,56,5,6]
p = 0


for i in arr:
    if i!=0:
        arr[p]= i
        p+=1

while p<len(arr):
     arr[p] = 0
     p+=1

print(arr)