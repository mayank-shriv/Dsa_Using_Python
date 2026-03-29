n = int(input())
arr = [int(input()) for _ in range(n)]

def mergeSort(leftSide, rightSide):
    p,q = 0,0
    
    result = []
    e, f = len(leftSide), len(rightSide)
    while(p<e and q<f):
        if leftSide[p]> rightSide[q]:
            result.append(rightSide[q])
            q+=1
        else:
            result.append(leftSide[p])
            p+=1
    result.extend(leftSide[p:])
    result.extend(rightSide[q:])
    return result

        
def merge(arr):
    
    l = len(arr)
    mid = l//2
    if l <= 1:
        return arr
    leftArray = arr[:mid]
    rightArray = arr[mid:]
    leftSide = merge(leftArray)
    rightSide = merge(rightArray)
    return mergeSort(leftSide, rightSide)
r = merge(arr)
print(r)                                                                                                                                                                                       