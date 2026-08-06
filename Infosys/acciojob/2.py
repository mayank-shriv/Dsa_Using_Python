# Remove All Occurrences of a Substring
# Given two strings str and K, perform the following operation on str until all occurrences of the substring K are removed:

# Find the leftmost occurrence of the substring K and remove it from str.
# Return str after removing all occurrences of K.

# A substring is a contiguous sequence of characters in a string.

# Input Format
# The first line of input contains the first string str.

# The second line of input contains the second string K

# Output Format
# Output is managed for you.

# Return string str after removing all occurrences of string K.

# -1 is printed if the final string is empty

# Example 1
# Input

# daabcbaabcbc
# abc
# Output

# dab
# Explanation

# The following operations are done:

# s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".

# s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".

# s = "dababc", remove "abc" starting at index 3, so s = "dab".

# Now s has no occurrences of "abc".

# Example 2
# Input

# axxxxyyyyb
# xy
# Output

# ab
# Explanation

# The following operations are done:

# s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".

# s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".

# s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".

# s = "axyb", remove "xy" starting at index 1 so s = "ab".

# Now s has no occurrences of "xy".

# Constraints
# 1 <= str.length <= 1000

# 1 <= K.length <= 1000

# s​​​​1​​ and K consists of lowercase English letters.


# brute force

class solution:
    def solve(self):
        s = input().strip()
        k = input().strip()



        while True:
            index_ele =  s.find(k)
            if index_ele == -1:
                break
            # Remove substring here
            s = s[:index_ele] + s[index_ele + len(k):]

        if s == '':
            print(-1)
        else:
            print(s)

obj = solution()
obj.solve()



# optimal
class Solution:

    def solve(self):

        s = input().strip()
        k = input().strip()

        stack = []

        for ch in s:
            stack.append(ch)
            if len(stack)>= len(k):
                if ''.join(stack[-len(k):]) == k:
                    for _ in range(len(k)):
                        stack.pop()
        ans = ''.join(stack)

        if ans == "":
            print(-1)
        else:
            print(ans)

obj = Solution()
obj.solve()



