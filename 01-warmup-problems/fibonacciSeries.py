# # 0,1,1,2,3,5,8
# def printFebonacci(numbers):
#     p=1
#     q=1

#     print(f'Fibonacci series :0, 1, 1, ',end="")
#     for i in range(numbers-3):
#         r=q+p
#         print(r,end=", ")
#         p=q
#         q=r


        
# printFebonacci(5)


# Recursion 
def FibonacciRecursion(number,p,q):
    if number==1 or number ==0:
        print(f'Fibonacci Series : 0' )
        return
    if number==2 :
        print("Fibonacci Series :",end="0, 1 ")
        return
   
    r=p+q
    print(r,end="")
    if number==3:
        return
    print(end=", ")
    FibonacciRecursion(number-1,p=q,q=r)

num=int(input("Enter the Number :"))
if num!=2 and num!=0 and num!=1:
    print(f'Fibonacci series :',end="0, 1, ")
FibonacciRecursion(num,0,1)
