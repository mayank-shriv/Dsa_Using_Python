# checking username 
# n = input("Enter the username:")
# valid = True

# if n.isalpha():
#     print(n)
# else:
#     print('username is invalid')


# check polidrome
# s = '## 45  ra  m  5  4  ##'
# cleaned = '' 

# for ch in s:
#     if s.isalpha():
#         cleaned+=ch.lower()
    
# if cleaned == cleaned[::-1]:
#     print("polindrome string")
# else:
#     print("string is not polindrome")


#optimal soln
s = input("Enter you string:")
def isPolindrome(s):
    clear = []
    s= s.lower()
    for ch in s:
        if ('a'<=ch<='z') or ('0'<=ch<='9'):
            clear.append(ch)
    clear = ''.join(clear)       
    print(clear)
    
    left = 0
    right = len(clear)-1
    while(left<right):
        if clear[left]!=clear[right]:
            return False
        left+=1
        right-=1
    return True
    

if isPolindrome(s):
    print("string is polindrome")
else:
    print("String is not polindrome")









# for ch in n:
#     if not ('a' <= ch <= 'z'):
#         valid = False
#         break

# if valid:
#     print('username is in lowercase')
# else:
#     print('username is in lowercase')