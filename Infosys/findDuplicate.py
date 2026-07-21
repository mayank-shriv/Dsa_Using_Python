# # here I will find duplicate number 

# try:
#     n = list(map(int, input().split()))
# except ValueError:
#     print("Invalid input: please enter integers separated by spaces")
#     exit(1)
# count = {}
# result = []
# for i in n:
#     if i not in count:
#         count[i]= 1
#     else:
#         count[i]+=1


# for k,v in count.items():
#     if v>1:
#         result.append(k)

# print(' '.join(map(str,result)))

# Duplicate characters in string
try:
    n = list(map(str, input().split()))
except ValueError:
    print("Invalid input: please enter letters separated by spaces")
    exit(1)
count = {}
result = []
for i in n:
    if i not in count:
        count[i]= 1
    else:
        count[i]+=1


for k,v in count.items():
    if v>1:
        result.append(k)

print(' '.join(result))