class Atm:
    def __init__(self,balance):
        self.__balance = balance  
# we are creating private variable using __ two underscore 

    def deposit(self, money):
        self.__balance += money

    def getBalance(self):
        print("Balance", self.__balance)
    
obj = Atm(2000)
obj.deposit(200)
obj.getBalance()
print(obj.__balance) #AttributeError 

# Security
# It uses naming conventions and name mangling to simulate private variables
