d = {1:'one',
     2:'two',
     3:'three',
     4:'four'
     }
print('dictionary',d)
#Insert and update 
# d[key] = value 
k = 5
d[k] = 'five'
print(f'For updating and inserting, we use d[key]= value {d}')

# d.get(k) It will return value at this index return None if missing

# d.get(key,0) returns 0 or default value 

print(f'By using get method u can find the value of key in a dict: {d.get(10,0)}')

# d.keys()

# d.values()

#d.items() used for iteration
# for key, value in d.items():

# del d[key] delete a key

# d.pop(key) #removes and returns value