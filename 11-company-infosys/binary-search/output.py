sum = 30
print("sum", sum) # Simple sum printing 

# f -string 
 
print(f'sum is {sum}')

#String Concatenation

print("sum = " + str(sum))


# .format()

print("sum is {}".format(sum))

# Printig list without brackets and commas space separated

list = [1,2,3,4,5]
print(*list) # 1 2 3 4 5

# Best method is .join

print('-'.join(map(str,list)))  # 1 2 3 4 5


print(list) # [1,2,3,4,5]


# Multiples output on separate lines 

for x in list:
    print(x)


# No space between values
a,b,c = 1,2,3
print(a, b,sep='') #12 
print(a,b)
print(a,end='') # No new line


# Custom separator 

print(a, b, c, sep=', ')  #1, 2, 3,


# If condition in print condition

print("yes" if a else "no")


#print a  number of digits after decimal number
d = 1.23222
print(f"{d:.2f}")   # :.

# alternative 
print(round(d,2))


# printing dictionary in key value pair

d = {a:1,b:2, c:3}
for k,v in d.items():
    print(k,":",v)