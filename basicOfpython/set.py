s = set()

# adding element in set
s.add(10)

# remove element from set  and raise error if number is missing
s.remove(10)

# No error if missing
s.discard(10)

# lookup 
if 10 in s:
    print("yes")
else: 
    print("No")


# Intersection s1 & s2
# Union s1 | s2
# Difference s1 - s2 