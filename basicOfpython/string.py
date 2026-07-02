s = 'Jai Shri Ram'

# Convert string to lowercase and print the result.
lower_s = s.lower()
print('After lower case method:', lower_s)

# Convert string to uppercase and print the result.
upper_s = s.upper()
print('After upper case method:', upper_s)

# Remove leading/trailing whitespace and print the result.
stripped_s = s.strip()
print('After strip (remove leading/trailing spaces):', stripped_s)

# Split into words by whitespace.
split_space = s.split()
print('Split by spaces:', split_space)

# Split by comma.
split_comma = s.split(',')
print('s.split(",") gives:', split_comma)

words = 'jai jai!!'
joined_words = '-'.join(words.split())
print('Join words with hyphens:', joined_words)

# Replace characters and print the result.
replaced_s = s.replace('a', 'b')
print('Replace a with b:', replaced_s)

# Returns first index of substring or -1.
find_index = s.find('abc')
print('find returned:', find_index)

# More useful string methods:
# - Remove all spaces: s.replace(' ', '')
# - Convert string to list of characters: list(s)
# - Convert string to list of words: s.split()
# - Remove leading/trailing spaces: s.strip()
# - Convert to title case: s.title()
# - Check if string is numeric: s.isdigit()
# - Count substring occurrences: s.count('a')
