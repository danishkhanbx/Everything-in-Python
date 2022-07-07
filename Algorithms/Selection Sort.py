# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The algorithm maintains two sub-arrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) from the
# unsorted subarray is picked and moved to the sorted subarray.

def sort(arr):
    for i in range(len(arr)):  # after one phase is completed element present at i=0 will be a sorted element
        # then i moves to the next index(i++) now only unsorted elements remains, i=0 will be excluded from now on
        min_index = i  # Find the minimum element in remaining unsorted array
        for j in range(i + 1, len(arr)):  # j=i+1 to j=len
            if arr[min_index] > arr[j]:  # means if i=0 is greater than j=1
                min_index = j  # then min will store value j index(1) value
        arr[i], arr[min_index] = arr[min_index], arr[i]  # i=0, j=1 swapped by i=1 and j=0

    return arr


arr = [99, 77, 66, 88, 33, 22, 11, 0]
sort(arr)
print(arr)
