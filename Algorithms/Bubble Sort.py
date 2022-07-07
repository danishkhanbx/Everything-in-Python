def sort(arr):
    for i in range(len(arr) - 1):  # Traverse through all array elements, len - 1 because outer loop will repeat one
        # time more than needed
        swapped = False
        for j in range(0, len(arr) - i - 1):  # Last i elements are already in place
            if arr[j] > arr[j + 1]:  # Swap the element, if right is founded smaller than the left element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # not swapped=not False=True, so if True it will break the i loop if no swap is done in j loop.
            break  # Time = O(n) for already sorted array.

    return arr


arr = [15, 20, 35, 49, 5, 36, 77]
sort(arr)
print(arr)
