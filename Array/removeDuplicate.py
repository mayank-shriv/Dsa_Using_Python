# # #brute force

def removeDuplicate(nums):
    n=len(nums)
    mydict = {}
    for i in range(0,n):
        mydict[nums[i]] = 0
    j  = 0
    for k in mydict:
        nums[j] = k
        j+=1
    print(f"Total number of unique no: ${j}")
    print(mydict.keys())


# # t(c) = o(2n) 

#optimized soln

def uniqueArrayCount(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i+1
    while j<n:
        if nums[j] != nums[i]:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
        j+=1

    return i+1
nums = [1,1,1,1,2,2,2,3,3,4,4,5]
print(uniqueArrayCount(nums))
removeDuplicate(nums)