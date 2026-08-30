# Problem: Book Allocation

# You are given an array where each element represents the number of pages in a book.

# Books = [12, 34, 67, 90]
# Students = 2

# Rules:

# Every student must get at least one book.
# Books must be assigned in order (contiguous).
# Minimize the maximum pages assigned to any student.

arr = list(map(int, input().split()))
students = int(input())


def canAllocate(students,arr, limit):
    studentCount = 1
    pages  = 0
    for book in arr:
        if pages + book <= limit:
            pages+= book
        else:
            studentCount += 1
            pages = book
            
        if studentCount > students:
                return False

    return True


def allocateBooks(arr, students):

    if students > len(arr):
        return - 1
    
    low = max(arr)
    high = sum(arr)  # Search space is 90 to 203
    answer = high
    while (low <= high):
        mid = (low + high) // 2

        if  canAllocate(students, arr, mid):
             answer = mid
             high = mid-1
        else: 
             low = mid + 1

    return answer

print(allocateBooks(arr, students))  

         