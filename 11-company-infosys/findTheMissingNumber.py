sumOfThisSeq = 0
n  = list(map(int, input().split()))
lastnum = (n[-1])
sum = (lastnum*(lastnum+1))//2
for i in n:
    sumOfThisSeq = sumOfThisSeq+i

print(sum - sumOfThisSeq)