arr1 = [1,1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7,8,9,10]
def mergeWithoutDupl(a1,a2):
    i,j = 0,0
    result =[]
    p,q = len(a1),len(a2)
    while (i<p and j<q):
        if a1[i]<= a2[j]:
            if  len(result)==0 or result[-1]!=a1[i] :
                result.append(a1[i])
            i+=1
        
        else :
            if  len(result) == 0 or result[-1]!=a2[j] :
                result.append(a2[j])
            j+=1
    while i<p:
        if result[-1]!=a1[i] or len(result) == 0:
            result.append(a1[i])
        i+=1
    while j<q:
        if result[-1]!=a2[j] or len(result) == 0:
            result.append(a2[j])
        j+=1

    return result
print(mergeWithoutDupl(arr2,arr1))