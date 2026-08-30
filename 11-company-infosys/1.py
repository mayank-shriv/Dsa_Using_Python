def soln(n):
    if (n==1):
        print("1", end=" ")
    while(n!=1):
        
        if (n%2==0):
            print(n//2, end=" ")
            n = n//2
        else:
            print((n*3)+1, end=" ")
            n= (n*3)+1
    
n = int(input())
soln(n)












# def input1(n):
#     if(n%2==0):
#         return n//2
#     else:
#         return (n*3)+1


# while True:
#     n = int(input("Enter the number:"))
#     print(input1(n))