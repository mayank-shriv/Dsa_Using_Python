nums = [5, 6, 9, 5]
freqMap = {}

for i in nums:
    if i in freqMap:
        # If the key exists, increment its value
        freqMap[i] += 1
    else:
        # If it's the first time, create the key with a value of 1
        freqMap[i] = 1

print(freqMap)


#get method 
num = [5, 6, 9, 5]
freqMap = {}

for i in nums:
    freqMap[i]=freqMap.get(i,0)+1
print(freqMap)


