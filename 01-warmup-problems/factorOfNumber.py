# class Factor:
#     def __init__(self,number):
#         self.number = number
#     def totalFactors(self):
#         fact= self.number
#         li=[i for i in range(1,fact+1) if fact%i==0]
#         print(li)
# n= int(input("Enter the NO :"))
# obj = Factor(n)
# obj.totalFactors() here time t(c)= o(n)

# we have another approach to make this code more faster.
from math import sqrt
class Factor:
    def __init__(self,number):
        self.number = number
        if self.number <0:
            print("Enter the positive No")
        self.factor= set()
    def totalFactors(self):
        number= self.number
        for i in range(1,int(sqrt(number)+1)):
            if number%i==0:
                self.factor.add(i)
                self.factor.add(number//i)
        sorted_list=list(sorted(self.factor))
        print(sorted_list)
count=0
while(True):
    n= int(input("Enter the NO :"))
    obj = Factor(n)
    obj.totalFactors()   #here time t(c)= o(n^(1/2))
    count+=1

