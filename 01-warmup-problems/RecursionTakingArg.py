# class recursion:
#     def Learn_recursion(self,num,times):
#         self.times=times
#         self.num =num
#         print(f'No is {self.num}')
#         self.times-=1
#         if self.times==0:
#             return
#         self.Learn_recursion(self.num,self.times)
        

# num=10
# obj1=recursion()
# obj1.Learn_recursion(num,times=3)

# print 1 to 10
# class recursion:
#     def Learn_recursion(self,st,num):
#         self.num =num
#         self.st=st
#         if self.num==0:
#             return
#         print(f'No is {self.st}')
        
#         self.Learn_recursion(self.st+1,self.num-1)



# num=10
# obj1=recursion()
# obj1.Learn_recursion(1,num)

# print n to 1
class recursion:
    def Learn_recursion(self,num,end):
        self.num =num
        self.st=st
        if self.num==0:
            return
        self.Learn_recursion(self.st+1,self.num-1)
        print(f'No is {self.num}')


num=10
obj1=recursion()
obj1.Learn_recursion(num,1)