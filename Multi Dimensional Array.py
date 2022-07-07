from numpy import *

"""
# 1-D
val = array([5, 7, 6, 3, 2, 0, 9, 1])  # implicitly given values type, explicitly any data type
print(val)
"""
# 2-D
arr1 = array([
    [1, 2, 3],
    [5, 6, 7]
])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 = arr1.flatten()  # convert from n-D to 1-D array
print(arr2)

arr3 = array([         # convert from n-D to m-D array
    [1, 2, 3, 6, 7, 8],
    [5, 6, 7, 0, 3, 1]
])

arr4 = arr3.reshape(3, 4)     # rows, columns
print(arr4)

arr5 = arr3.reshape(2, 2, 3)  # 2 2-D array inside a 3-D Array
print(arr5)
