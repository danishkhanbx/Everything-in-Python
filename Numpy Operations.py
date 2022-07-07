from numpy import *

"""
## Creating Arrays ##

# array()
arr1 = array([5, 7, 6, 3], float)
print(arr1)

# linspace()
arr2 = linspace(0, 15, 16)  # starting(included), ending(included), number of ways it can be divided
print(arr2)

# arange()
arr3 = arange(1, 15, 2)  # starting(included), ending(included), spacing between two numbers
print(arr3)

# logspace()
arr4 = logspace(1, 40, 5)  # 10^starting(included), 10^ending(included), divided into parts
print(arr4)
print('%.2f' % arr4[0])
print('%.2f' % arr4[4])

# zeros() and ones()
arr5 = zeros(5)
arr6 = ones(5, int)  # implicitly float, explicitly any data type
print(arr5, arr6)
"""

"""
## Operations on array ##

# Addition & Subtraction
arr = array([1, 2, 3, 4, 5])
arr = arr + 5
print(arr)

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([1, 2, 3, 4, 5])
arr3 = arr1 + arr2
print(arr3)

# inbuilt functions
print(sum(arr1))   # min, max, avg, etc
print(sin(arr1))   # cos, tan, sinh, cosh, etc
print(log(arr1))   # e, pi, etc
print(sqrt(arr1))  # ceil, floor, pow, etc
print(sort(arr1))  # reverse, etc
print(concatenate([arr1, arr2]))  # compare, etc
"""

## Copying an Array ##
ar1 = array([1, 2, 9, 8, 5])
ar2 = ar1
print(ar1, id(ar1))
print(ar2, id(ar2))

# view - shallow copy
a1 = array([1, 2, 9, 8, 5])
a2 = a1.view()
a1[1] = 7
a2[2] = 67
print(a1, id(a1))  # different address's, but when one array value is mutated the other array got mutated too
print(a2, id(a2))

# copy - deep copy
b1 = array([1, 2, 9, 8, 5])
b2 = b1.copy()
b1[1] = 7
b2[2] = 67
print(b1, id(b1))  # different address's, and when one array value is mutated it does not affect the other arrays
print(b2, id(b2))
