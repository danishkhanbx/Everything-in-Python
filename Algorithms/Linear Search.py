def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


arr = [15, 20, 35, 49, 5, 36, 77]
key = int(input('Enter the key to Searched: '))
index = search(arr, key)
if index == -1:
    print('Key not found')
else:
    print('Key found at index', index+1)

