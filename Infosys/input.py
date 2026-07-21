# Input 10 20 30 40  50 
# n = list(map(int, input().split()))
# print(n)

# output [10, 20, 30, 40, 50]

# 10,20,30,40,50 
# n = list(map(int, input().split(',')))
# print(n)


# output [10, 20, 30, 40, 50]

# we are taking two input first one is row amd second is colm

# i/p 2,3

# row, colm  = map(int, input().split(','))
# print(row, colm)

# # ip str 1 or str 2
str1 = "abcde"
str2 = "e"
def removestring(str1,str2):
    result = []
    for ch in str1:
        if ch not in str2:
            result.append(ch)


    return "-".join(result)
print(removestring(str1,str2))


# n = int(input())
# arr = list(map(int, input().split()))

# count = {}

# for i in arr:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1

# result = []

# for k, v in count.items():
#     if v == 1:
#         result.append(k)

# print(" ".join(map(str, result)))

## 
# n = list(input().split())
# n1 = input().split()
# n2 = list(map(int, input().split())) #isko list me convert karna padega map ke karan
# r = '2212323'
# n3 = " ".join(r)
# print(n)
# print(n1)
# print(n2)
# print(n3)