# Check whether the string is polindrome or not?

str_input = str(input("Enter the string ")).strip().lower()
result = []
for i in str_input:
    if ('a' <= i <= 'z') or ('0' <= i <= '9'):
        result.append(i)

print(''.join(result))

left = 0
right = len(result) - 1
is_palindrome = True

while left < right:
    if result[left] != result[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")


















# class Palindrome:
#     # The __init__ method should accept the number and store it
#     def __init__(self, number):
#         self.original_number = number

#     def check(self):
#         # Use the number stored in the instance
#         number = self.original_number
#         reversed_sum = 0
        
#         # This loop correctly reverses the number
#         while(number > 0):
#             last_digit = number % 10
#             reversed_sum = reversed_sum * 10 + last_digit
#             number = number // 10
            
#         # Compare the reversed number with the original number
#         if self.original_number == reversed_sum:
#             print(f'{self.original_number} is a palindrome number.')
#         else:
#             print(f'{self.original_number} is not a palindrome number.')


# # Get input from the user
# n = int(input("Enter the No to check palindrome or not: "))

# # Create an object, passing the number 'n' to the constructor
# obj1 = Palindrome(n)

# # Call the check method
# obj1.check()