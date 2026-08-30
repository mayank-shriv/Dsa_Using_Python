# Check weather a number is armstrong or not?

num = int(input("Enter the number: "))

def check_armstrong(num):
    if num < 0:
        print("Please enter a positive number")
        return

    digits = str(num)
    power = len(digits)

    total = 0
    for digit in digits:
        total += int(digit) ** power

    if total == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

check_armstrong(num)



# import math
# class armstrong:
#     def __init__(self,number):
#         self.number = number
#     def ArmstrongCheck(self):
#         number=self.number
#         sum=0
#         while(number>0):
#             lastNum=number%10
#             sum=(lastNum**3)+sum
#             number=number//10
#         if (self.number==sum):
#             print(f'{self.number} is armtrong no')
#         else:
#             print(f'{self.number} is not armstrong no')

# n=int(input("Enter the no to check wheather is a armstrong no or not? :"))
# obj = armstrong(n)
# obj.ArmstrongCheck()