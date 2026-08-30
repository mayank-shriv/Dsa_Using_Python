list = [1,2,3,4,5,6,6]
# #brute force
# def secondLargest(list):
#     list.sort()
#     return list[-2]
# print(f'the second largest number is : {secondLargest(list)}')


#second way

# def secondLargest(list):
#     secondLargest = -float("inf")
#     largest = -float("inf")
#     for i in list:
#         if largest<i:
#     #         largest=i
    
    # for p in list:
    #     if secondLargest < p and p !=largest:
    #         secondLargest = p
    # # print(f'second largest number is : {secondLargest}')

# tc = O(n+n) ~ O(n)
# sc O(1) constant

# optimal soln
def secondLargest(list):
    secondLargest = -float("inf")
    largest = -float("inf")
    n=len(list)
    for i in range(0,n):
        if list[i]>largest:
            secondLargest = largest
            largest = list[i]
        elif list[i]>secondLargest and list[i]!=largest:
            secondLargest = list[i]
    print(f'the second largest element is : {secondLargest}')
secondLargest(list)  

tc = O(n)
sc = O(n)