# Input ways

# Normal way 

n = input() #This way is good for string

# For integers

n = int(input())



# For float

n = float(input())

# Two integer on the same line

n,m = map(int, input().split())  # split will split these numbers based on space between them then map will convert these two into integers.

# Three or more integers on the same line
 
o,p,q = map(int, input().split())


# array / list of integers

arr = list(map(int, input().split())) #If input is like this 1 2 3 4 5 

# comma separated
arr = list(map(int, input().split(','))) # If input is like this 1, 2, 3, 4, 5


# Array of string

words = input().split() # apple banana cherry

# For example input like this (Two lines)

# 1 2 3 4 5 6 
# 3

n = list(map(int, input().split()))
n1 = int(input())

# 1, 2 ,3, 4, 5
# 3

n = list(map(int, input().split('')))
n1 = int(input())


# Number of test cases, then that many lines
# 4
# 1 3 
# 1 4
# 2 5
# 3 5

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)

# Input:
# 3
# 10
# 20
# 30

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


# Input:
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

row, col = map(int, input().split())
arr = []
for i in range(row):
    for j in range(col):
        row = list(map(int, input().split()))
        arr.append(row)


# Input:  John 25 5.9
name, age, height = input().split()
age = int(age)
height = float(height)


# Input:
# 1 2
# 3 4
# 5 6
# (end of file)


# Unknown number of inputs until EOF (no fixed count given)
import sys
lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a + b)


# 18. Reading all input at once and splitting
# Input:
# 1 2 3
# 4 5
# 6
# python
# import sys
# data = sys.stdin.read().split()
# data = list(map(int, data))
# # now slice data as needed based on problem

# This is useful when you don't know how the lines are broken up, but know the total sequence of numbers.


#########################################################################################
# output ways

# Print list as space-separated values (not brackets)
arr = [1, 2, 3]
print(*arr)
# Output: 1 2 3


print(','.join(map(str, arr)))

# Output: 1,2,3



# Print with custom separator

print(1, 2, 3, sep=', ')
# Output: 1, 2, 3  #best 


# Print without new line
print("hello",end='')
print("mayank")

# Print formating string 

name = "Mayank Shrivastava"
age = 20
print(f'My name is {name} and I am {age} years old')


# Print number after . 
number = 23.232
print(f'{number:.2f}')