# A company has several jobs. Each job has a start time and an end time.

# Only one job can run at a time.

# Find the maximum number of non-overlapping jobs that can be completed.

# start = [1, 2, 4, 6, 5, 8]
# end   = [3, 5, 5, 7, 9, 10]

start = list(map(int, input().split()))
end = list(map(int, input().split()))

def maximumMetting(start,end):
    lenOfStart = len(start)
    arr = []
    for i in range(lenOfStart):
        arr.append((end[i],start[i]))
    # [(3,1),(5,2),(5,4),(7,6),(9,5),(10,8)]
    arr.sort()  # O(nlogn)
    # [(3,1),(5,2),(5,4),(7,6),(9,5),(10,8)]
    lastItem = -1
    count = 0

    for end,start in arr:
        if start > lastItem:
            count+=1
            lastItem = end

    return count
        

print(maximumMetting(start,end))


    

        