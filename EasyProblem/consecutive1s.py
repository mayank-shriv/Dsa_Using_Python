nums = [1,0,1,1,1,1]
l = len(nums)

max_count = 0  # Renamed 'max'
count = 0      # You were missing this initialization

for i in range(0, l):
    if nums[i] == 1:
        # If we see a 1, increment the current count
        count += 1
    else:
        # If we see a 0, reset the current count
        count = 0  # Bug 2: Was '==' (comparison), changed to '=' (assignment)

    # After every number, check if the current count 
    # is the new maximum count.
    if max_count < count:
        max_count = count

print(max_count)