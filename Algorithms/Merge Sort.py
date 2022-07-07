def merge_sort(arr):
    if len(arr) <= 1:  # when there is one or fewer elements
        return

    mid = len(arr) // 2
    left = arr[:mid]   # 0 to mid-1
    right = arr[mid:]  # mid to len(arr)

    # Finding the mid of the passed array. The mid will lead to the creation of 2 separate array lists sending the first
    # and second half separately of the array to get divided again and again till reaches 1 element in returning time we
    # will start comparing the elements and sorting them. First 2-2 lists of elements then 4-4 lists of elements & so on
    # Calling time we divide till 1 Returning time we compare(sort) and merge.

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0  # i,j,k are index pointers. i points to array a, j to array b, and k to array arr

    while i < len_a and j < len_b:  # stopping when reached either end of the lists
        if a[i] <= b[j]:          # array a value is less, than add it to the array arr and increment a++ index pointers
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1        # of the two conditions one will be true, & in each array arr pointer k will be incremented++

    while i < len_a:  # when either one of the lists ended, we copy the remaining elements of(either a or b) in arr
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    merge_sort(elements)
    print(elements)
