# Program to print all combination of size r in an array of size n

# The main function that prints all combinations of size r in arr[] of size n. Function mainly uses combinationUtil().
def printCombination(arr, n, r):
    # A temporary array to store all combination one by one
    data = [0] * r  # data = [0, 0]

    # Print all combination using temporary array 'data[]'
    combinationUtil(arr, n, r, 0, data, 0)


# arr[] ---> Input Array
# n     ---> Size of input array
# r     ---> Size of a combination to be printed
# index ---> Current index in data[]
# data[] ---> Temporary array to store current combination
# i     ---> index of current element in arr[]
def combinationUtil(arr, n, r, index, data, i):
    # Current combination is ready, print it
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return

    # When no more elements are there to put in data[]
    if i >= n:
        return

    # current is included, put next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1, data, i + 1)

    # current is excluded, replace it with next (Note that i+1 is passed, but index is not changed)
    combinationUtil(arr, n, r, index, data, i + 1)


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3]
    r = 2
    n = len(arr)
    printCombination(arr, n, r)


'''
For example,
arr = [1, 2, 3]
r = 2
n = len(arr) = 3

printCombination(arr, n, r) = ([1,2,3], 3, 2) --> data = [0]*r = [0, 0] -->

combinationUtil(arr, n, r, index=0, data, i=0) = ([1,2,3], 3, 2, 0, [0,0], 0) -->

if: index == r --> 0 == 2 = False
if i >= n --> 0 >= 3 = False
data[index=0] = arr[i=0] --> data = [1, 0]
combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 1, [1,0], 1) -->

1 == 2 = False
1 >= 3 = False
data[index=1] = arr[i=1] --> data = [1, 2]
combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 2, [1,2], 2) -->

2 == 2 = True, print data = [1,2], return 
--> combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 1, [1,2], 1) 
combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 1, [1,2], 2) --> 

1 == 2 = False
2 >= 3 = False
data[index=1] = arr[i=2] --> data = [1, 3]
combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 2, [1,3], 3) -->

2 == 2 = True, print data = [1,3], return 
--> combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 1, [1,3], 2) 
combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 1, [1,2], 3) --> 

1 == 2 = False
3 >= 3 = True, return
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 1, [1,2], 2) 
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 1, [1,2], 1) 
--> combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 0, [1,0], 0) 
combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [1,2], 1) -->

0 == 2 = False
if i >= n --> 1 >= 3 = False
data[index=0] = arr[i=1] --> data = [2, 3]
combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 1, [2,3], 2) -->

1 == 2 = False
if i >= n --> 2 >= 3 = False
data[index=1] = arr[i=2] --> data = [2, 3]
combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 2, [2,3], 3) -->
index == r --> 2 == 2 = True, print data = [2,3], and return
--> combinationUtil(arr, n, r, index + 1, data, i + 1) = ([1,2,3], 3, 2, 1, [2,3], 2)
combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 1, [2,3], 3) -->

1 == 2 = False
3 >= 3 = True, return
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 1, [2,3], 2) 
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [2,3], 1) 
combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [2,3], 2) -->

0 == 2 = False
2 >= 3 = False
data[index=0] = arr[i=2] --> data = [3, 3]
combinationUtil(arr, n, r, index+1, data, i + 1) = ([1,2,3], 3, 2, 1, [3,3], 3) -->

1 == 2 = False
3 >= 3 = True, return 
--> combinationUtil(arr, n, r, index+1, data, i + 1) = ([1,2,3], 3, 2, 0, [3,3], 2)
combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [3,3], 3) -->

0 == 2 = False
3 >= 3 = True, return 
--> combinationUtil(arr, n, r, index+1, data, i + 1) = ([1,2,3], 3, 2, 0, [3,3], 2)
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [3,3], 1)
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [3,3], 1)
--> combinationUtil(arr, n, r, index, data, i + 1) = ([1,2,3], 3, 2, 0, [3,3], 0)

--> combinationUtil(arr, n, r, 0, data, 0)
--> printCombination(arr, n, r)

'''


