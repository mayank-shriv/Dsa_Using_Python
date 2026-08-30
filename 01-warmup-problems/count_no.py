# n = int(input("Enter the no to count:"))
# count=0
# while(n>0):
#     lastDigit = n%10
#     print(lastDigit,end='')
#     n=n//10
#     count+=1
# print(end='\n')
# print(f'Total no is {count}')


class countNo:
    def __init__(self, number):
        self.number = number
    def reverseNo(self):
        count=0
        number=self.number
        print("Reverse Digit :",end=" ")
        while (number>0):
            lastNumber = number%10
            print(lastNumber,end='')
            number = number//10
            count+=1
        print(end='\n')
        print(count)    
n=int(input("enter the no:"))
obj1 = countNo(n)
obj1.reverseNo()