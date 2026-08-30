def sum(i,sum1,n):
    sum1=sum1+i
    if i>=n:
        print(f'sum is {sum1}')
        return
    sum(i+1,sum1,n)

sum(i=1,sum1=0,n=5)


#functional recursion
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

n1=sum(5)
print(n1)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n1=fact(5)
print(n1)

