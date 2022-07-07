# Quotes
print('spam eggs')  # single quotes
print('doesn\'t')  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')
print("'Isn\"t,' they said.")

# Special characters
print()
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output (only in terminal)
print(s)  # with print(), \n produces a new line
# r: ignores special characters in the string
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# Operators in string
print()
str1 = 3 * "hi "
print(str1)
str2 = "hi, " + "how are you?"
print(str2)
str3 = "yo" " dude"
print(str3)
str = ('Put several strings within parentheses '
       'to have them joined together.')
print(str)
prefix = "Py"
print(prefix + 'thon')

## String as Arrays:
word = 'Python'

# 1. Indexing
print()
print(word[0])  # character in position 0
print(word[5])  # character in position 5
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])  # Note that since -0 is the same as 0, negative indices start from -1.

# 2. Substrings
print()
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
# Note: How the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s.
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[4:42])  # out of range slice indexes are handled gracefully
print(word[42:])  # this prints space as there exists nothing
print(word[:2] + 'py')
str4 = 'J' + word[1:]
print(str4)
print(len(word))

# Errors in String
# 1. try to access an undefined variable
# print(n)
# 2. invalid syntax
# prefix = 'Py'
# print(prefix 'thon') # can't concatenate a variable and a string literal
# ('un' * 3) 'ium'
# 3. the word only has 6 characters
# print(word[42])
# 4. object does not support item assignment
# word[0] = 'J'
# word[2:] = 'py'
