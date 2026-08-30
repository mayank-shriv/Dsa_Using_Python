# Problem 4 — Minimum Processing Speed

# A data-processing system has N batches of tasks.

# batches = [3, 6, 7, 11]
# H = 8

# The processor works at a fixed speed of K tasks per hour.

# For each batch:
# It processes at most K tasks in one hour.
# It works on only one batch at a time.
# If a batch contains fewer than K remaining tasks, it finishes that batch in that hour and starts the next batch in the next hour.

# Find the minimum value of K such that all batches can be completed within H hours.

arr = list(map(int, input().split())) 
hours = int(input())

def checkCapacity(capacity, arr, hours):
    hourCount = 0

    for batch in arr:
        hourCount += (batch + capacity - 1) // capacity

        if hourCount > hours:
            return False

    return True

    

def  taskCapacity(arr, hours):
    low = 1
    high = max(arr)
    answer = 0
    while(low<=high):
        capacity = (low + high)//2
        if  checkCapacity(capacity, arr, hours):
            answer = capacity
            high = capacity -1
        else:
            low = capacity + 1

    return answer


print(taskCapacity(arr, hours))
