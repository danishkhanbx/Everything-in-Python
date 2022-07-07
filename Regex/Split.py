from re import *

# spilt: Splits the string from the given pattern
# Syntax: split('pattern', source_string, maxsplit(optional))
str = 'Danish Khan'
str1 = 'Danish Khan is lost in thinking'
x = split("Khan", str)
y = split('a', str)
z = split(" ", str)
a = split('', str1)
b = split(' ', str1, 2)
print(x)
print(y)
print(z)
print(a)
print(b)
