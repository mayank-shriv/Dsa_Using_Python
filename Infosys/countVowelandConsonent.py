str_input = input("Enter the string : ").strip().lower()
s = {'a', 'e', 'i', 'o', 'u'}
countVow = 0
countConsonent= 0
for ch in str_input:
    if ch.isalpha():
        if ch in s:
            countVow+=1
        else:
            countConsonent+=1

print(f'Number of consonent in str: {countConsonent}')
print(f'Number of vowel in str: {countVow}')