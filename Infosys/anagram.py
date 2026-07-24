s1, s2 = input().split()

if len(s1) != len(s2):
    print("Not Anagram")
    exit()

for ch in s1:
    if s1.count(ch) != s2.count(ch):
        print("Not Anagram")
        exit()

print("Anagram")