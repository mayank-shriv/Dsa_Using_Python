# Basic list methods
# Use append to add an element at the end.
arr = []

arr.append(10)
print('append:', arr)

# We can add multiple elements at once using extend.
arr.extend([20, 30,40,50,60,67,65,43,46,23,63,56])
print('extend:', arr)

# It returns the index of the value.
print('index_value:', arr.index(30))

# Insert an element at a specific position using insert(index, value).
arr.insert(3, 40)
print('insert at specific location:', arr)

# Remove the element at the end.
arr.pop()
print('pop:', arr)

# Remove the element at a specific position.
arr.pop(2)
print('pop at specific pos:', arr)

# Membership test.
if 10 in arr:
    print('membership operator IN')

# Remove the first occurrence of the value.
arr.remove(10)
print('after remove(10):', arr)

# Delete by index.
del arr[0]
print('delete by index:', arr)

# Count occurrences.
count_5 = arr.count(5)
print('count of 5:', count_5)

# Sort in ascending order.
arr.sort()
print('print sorted arr in place sorting:', arr)

# Sort in descending order.
arr.sort(reverse=True)
print('sort in place in desc:', arr)

# Return a new sorted list.
sorted_arr = sorted(arr)
print('sorted new arr sorted(arr):', sorted_arr)

# Reverse in place.
arr.reverse()
print('reversed arr in place:', arr)

# Return a reversed copy.
print('reverse arr copy arr[::-1]:', arr[::-1])



# Remove everything.
arr.clear()
print('after clear:', arr)