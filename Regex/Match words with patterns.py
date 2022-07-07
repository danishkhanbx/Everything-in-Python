from re import *

str = 'Sat, hat, mat, pat'

# allstr = findall('[shmp]at', str)  # Output: hat mat pat
# allstr = findall('[Shmp]at', str)  # Output: Sat hat mat pat
# allstr = findall('[h-m]at', str)   # Output: hat mat
# allstr = findall('[h-z]at', str)   # Output: hat mat pat
allstr = findall('[^h-m]at', str)    # Output: Sat pat
for i in allstr:
    print(i)
