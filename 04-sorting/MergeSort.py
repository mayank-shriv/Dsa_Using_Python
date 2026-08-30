# Merge Sort 
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    leftArray = arr[:mid]
    rightArray = arr[mid:]
    left = mergeSort(leftArray)
    right = mergeSort(rightArray)
    return merge(left,right)
def merge(list1, list2):
    p,q = 0,0
    n,m = len(list1), len(list2)
    result = []
    while p<n and q<m:
        if list1[p]>list2[q]:
            result.append(list2[q])
            q+=1
        else:
            result.append(list1[p])
            p+=1
    while p<n:
        result.append(list1[p])
        p+=1  
    while q<m:
        result.append(list2[q])
        q+=1
    return result

list1 = [12,23,435,456,5657,43435,102,213,1,1,2,312,1231,2312]
print(mergeSort(list1))
