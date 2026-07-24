str_input = input()  # abcbdjfj
seen = {}
left = 0
max_len = 0
start = 0

for right in range(len(str_input)):
    char = str_input[right]
    if char in seen and seen[char] >= left:
        left = seen[char] + 1
    seen[char] = right
    if right - left + 1 > max_len:
        max_len = right - left + 1
        start = left

print(str_input[start:start + max_len])
print(max_len)