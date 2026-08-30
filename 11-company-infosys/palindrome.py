
# A num is prime or not?
# from math import sqrt


# class Prime:
#     def __init__(self,n):
#         self.number = n
    
#     def isPrime(self):
#         if self.number == 2 or self.number == 3:
#             print(f"Num is prime number")
#             return
#         if self.number <=1:
#             print("Number is not prime number")
#             return
#         root = int(sqrt(self.number))
#         for i in range(2,root+1):
#             if self.number%i == 0:
#                 print("Number is not prime")
#                 return
        
#         print("Number is prime")

# n = int(input("Enter the Num:"))
# obj = Prime(n)      
# obj.isPrime()





# # palindrome num 121

# n = int(input())
# sum = 0
# k = n
# while(n>0):
    
#     n1 = n%10
#     sum = sum*10+n1
#     n = n//10
# if k == sum:
#     print(sum, "is palindrome num")