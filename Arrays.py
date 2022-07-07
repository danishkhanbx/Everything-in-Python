from array import *  # import array as arr

val = array('i', [5, 7, 6, 3, 2, 0, 9, 1])  # for character array('u', ['a', 'b', 'c', 'd'])
print(val)

"""
# inbuilt functions
print(val.buffer_info())  # prints address, size of the array
print(val.typecode)       # data type of the array
val.reverse()             # reversing takes 2 steps
print(val)
print(val[0])
for i in range(len(val)):   # or for e in val:
    print(val[i])           # print(e)

# Copying an Array
print()
newArr = array(val.typecode, (a for a in val))  # val.typecode to dynamically find the type of 
for e in newArr:                                # and a for a to copy it the values one by one into the new array
    print(e)                                    # a*a for a in val will print [1, 81, 0, 4, 9, 36, 29, 25]
"""

# input in array
arr = array('i', [])
n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
print(arr)

search = int(input("Enter value to be searched: "))
k = 0  # or print(arr.index(search)) it will print the index of the key to be searched directly no loop needed
for e in arr:
    if e == search:
        print("Index: ", k)
    k += 1
