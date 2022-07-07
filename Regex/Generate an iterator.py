from re import *

str = 'we need to inform him with the latest information'
for i in finditer('info', str):
    location = i.span()  # match object span: tuple the start and end positions of match
    print(location)

# we need to inform him with the latest information
# 12 3456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO
# a = 9 + a = 9 + 1 = 10
# e = 14, j = 19, o = 24, t = 29, y = 34, z = 35
# A = 36, E = 40, J = 45, O = 50, T = 55, Y = 60, Z = 65
