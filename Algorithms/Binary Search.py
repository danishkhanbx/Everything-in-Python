# Iterative Binary Search Function.
# It returns index of x in given array arr if present, else returns -1
"""
def search(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:  # If x is greater, ignore left half
            low = mid + 1
        elif arr[mid] > key:  # If x is smaller, ignore right half
            high = mid - 1
        else:   # means x is present at mid
            return mid

    return -1


arr = [1, 2, 3, 6, 9, 10]
key = int(input('Enter the key to Searched: '))
index = search(arr, key)
if index == -1:
    print('Key not found')
else:
    print('Key found at index', index + 1)
"""


# Recursive binary search.
# Returns index of x in arr if present, else -1
def search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:  # If element is present at the middle itself
            return mid
        elif arr[mid] > key:  # If element is smaller than mid, then it can only be present in left subarray
            return search(arr, low, mid-1, key)
        else:   # Else the element can only be present in right subarray
            return search(arr, mid+1, high, key)
    else:  # Element is not present in the array
        return -1


arr = [1, 2, 3, 6, 9, 10]
key = int(input('Enter the key to Searched: '))
index = search(arr, 0, len(arr)-1, key)
if index == -1:
    print('Key not found')
else:
    print('Key found at index', index + 1)
