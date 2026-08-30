class StringPalindrome:
    def __init__(self, left, right, s):
        self.left = left
        self.right = right
        self.s = s

    def checkPalindrome(self):
        # Base case: crossed or met in the middle₹
        if self.left >= self.right:
            return True
        # If mismatch found
        if self.s[self.left] != self.s[self.right]:
            return False
        # Move inward and check again
        self.left += 1
        self.right -= 1
        return self.checkPalindrome()


# Input from user
python_string = input("Enter the string to check whether it is a palindrome: ")
obj = StringPalindrome(0, len(python_string) - 1, python_string)
check = obj.checkPalindrome()

print(f"This string is {'a' if check else 'not'} palindrome")
