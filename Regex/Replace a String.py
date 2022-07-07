from re import *

# sub: substitute new string to old string
# Syntax: sub('old pattern', 'new pattern', source_string, replace only for the first n no. of occurrences (optional))

# Replacing a word
food = 'hat rat mat pat'

regex = compile('[r]at')
food = regex.sub('food', food)
print(food)

# Replacing spaces
str = '''
Hello my friend
How are you
feeling good today
'''
print(str)

# removing new line space with a space
regex = compile('\n')
str = regex.sub(' ', str)
print(str)

# we can all work with other space special characters
# \b : backspace
# \f : formfeed
# \r : carriage return
# \t : tab
# \v : vertical tab
