list=[1,3,5,7,8,31,53]
# r=len(list)-1
# l=0
def arrayReverse(list,left,right):
    if left>=right:
        return 
    list[left],list[right]=list[right],list[left]
    arrayReverse(list,left+1,right-1)

def reversearrayatperticularplace(list,l,r):
    arrayReverse(list,l,r)
    print(list)
reversearrayatperticularplace(list,3,6)