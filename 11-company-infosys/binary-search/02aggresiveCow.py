stalls = [1, 2, 4, 8, 9]
cows = 3
stalls.sort()

def check(stalls, cow, distance):
    cowCount = 1
    if cow > len(stalls):
        return False

    lastPosition = stalls[0]

    for i in range(1,len(stalls)):
        if stalls[i]-lastPosition >= distance:
            lastPosition = stalls[i]
            cowCount+=1

        if cowCount == cow:
            return True

    return False

def aggressiveCowArrangement(stalls, cows):

    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0

    while low <= high:

        mid = (low + high) // 2

        if check(stalls, cows, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer

print(aggressiveCowArrangement(stalls, cows))