from re import *

# search returns match object if there are any matches. There are three match objects
# Syntax: search('pattern', source_string)
# 1. start: gives the position and occurrence
# 2. span: tuple the start and end positions of match
# 3. string: return the actual string used for pattern matching
if search('inform', 'we need to inform him with the latest information'):
    print('There is inform')

str = 'Danish Khan'
x = search("a", str)
y = search("Khan", str)
z = search("D", str)
print(x.start(), '\n', y.start(), '\n', z.start())
print(x.span(), '\n', y.span(), '\n', z.span())
print(x.string, '\n', y.string, '\n', z.string)


# findall returns list of all matches
# Syntax: findall('pattern', source_string)
allinform = findall('inform', 'we need to inform him with the latest information')
for i in allinform:
    print(i)

