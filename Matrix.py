from numpy import *

arr1 = array([
    [1, 2, 3, 6],
    [5, 6, 7, 8]
])

m1 = matrix(arr1)
print("Matrix1:")
print(m1)

m2 = matrix('1 2 3 6 ; 4 5 8 9')  # create a matrix of 2 rows and 4 columns
print("Matrix2:")
print(m2)

m3 = matrix('1 2 3; 4 5 6 ; 7 8 9')  # create a matrix of 3 rows and 3 columns
print("Matrix3:")
print(m3)
print("Diagonal Elements: ", diagonal(m3))
print(m3.min())  # max, ...

m4 = m3 + m3
m5 = m3 * m3
print("Matrix4:")
print(m4)
print("Matrix5:")
print(m5)
