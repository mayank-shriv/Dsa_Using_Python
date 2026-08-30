# Count Subarrays with given Sum
# Given an unsorted array arr[] of N integers and a sum. The task is to count the number of subarrays which adds to a given number.

# Try using map

# Note: Use binary search to solve the problem

# Input Format
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.

# Each test case contains an integer N denoting the size of the array and integer denoting the value of the sum in the first line.

# The next line contains N space separated integers forming the array.

# Output Format
# For each testcase, if the element is present in the array print "1" (without quotes), else print "-1" (without quotes).

# Example 1
# Input


# 2
# 5 -10
# 10 2 -2 -20 10
# 6 33
# 1 4 20 3 10 5




# Output

# 3
# 1

# Explanation


#  Testcase 1: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].

#  Testcase 2: Subarray with sum 33 is: [20, 3, 10].

# Constraints:

# 1 <= T <= 100

# 1 <= N <= 10^4

# -10^5 <= arr[i] <= 10^5

# -10^5 <= sum <= 10^5

# Note:- Sum of N over all test cases does not exceed 10^5

class Solution:

    def countSubarray(self, arr, target):

        prefixSum = 0
        count = 0
        seen = {0: 1}

        for num in arr:
            prefixSum += num

            count += seen.get(prefixSum - target, 0)

            seen[prefixSum] = seen.get(prefixSum, 0) + 1

        return count

    def solve(self):

        t = int(input())

        for _ in range(t):

            n, target = map(int, input().split())

            arr = list(map(int, input().split()))

            ans = self.countSubarray(arr, target)

            if ans == 0:
                print(-1)
            else:
                print(ans)


if __name__ == "__main__":
    solution = Solution()
    solution.solve()



    
class Solution:
    def solve(self):

        t = int(input())

        for _ in range(t):

            n, target = map(int, input().split())

            arr = list(map(int, input().split()))

            prefixSum = 0
            count = 0
            seen = {0: 1}

            for num in arr:
                prefixSum += num

                count += seen.get(prefixSum - target, 0)

                seen[prefixSum] = seen.get(prefixSum, 0) + 1

            if count == 0:
                print(-1)
            else:
                print(count)


if __name__ == "__main__":
    solution = Solution()
    solution.solve()

def checkTarget(arr, target):
    if not arr:
        return -1

    prefixSum = 0
    count = 0

    # Stores: prefixSum -> frequency
    seen = {0: 1}

    for num in arr:
        prefixSum += num

        if (prefixSum - target) in seen:
            count += seen[prefixSum - target]

        seen[prefixSum] = seen.get(prefixSum, 0) + 1

    if count == 0:
        return -1

    return count



t = int(input())

for _ in range(t):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))

    print(checkTarget(arr, target))


class Solution:
    def countSubarrays(self, arr, target):
        prefixSum = 0
        count = 0

        # Stores prefixSum -> frequency
        seen = {0: 1}

        for num in arr:
            prefixSum += num

            if (prefixSum - target) in seen:
                count += seen[prefixSum - target]

            seen[prefixSum] = seen.get(prefixSum, 0) + 1

        return count


# Driver Code
t = int(input())

for _ in range(t):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.countSubarrays(arr, target))
