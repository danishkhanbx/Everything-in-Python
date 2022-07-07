# Algorithm:
# Select pivot, low, and high elements.
# Keep moving low & high pointers until we found the indexes which satisfies the conditions:
#  A[low] > A[pivot] and A[high] <= A[pivot]
#  If low < high then swap A[low] with A[high] and
#  If low >= high then swap A[pivot] with A[high]

def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


# Hoare partition
def partition(elements, start, end):
    pivot_index = start  # taking the first index(0) as a pivot in Hoare's partition
    pivot = elements[pivot_index]  # pivot index value
    while start < end:  # these while loops will stop at the index which satisfies the conditions
        while start < len(elements) and elements[start] <= pivot:  # start < size and start value <= pivot value
            start += 1  # incrementing start index pointer, i.e. start points to index 2 now, if it pointed to 1 before

        while elements[end] > pivot:  # it will stop when pivot value > then end value, so we have found the index
            end -= 1  # decrementing end index pointer, i.e. end points to index 5 now, if it pointed to 6 before

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)  # when end >= start, swapping end with pivot, the pivot value at end index will be
    return end  # sorted element, which is at its perfect index


def partitions(elements, start, end):
    pivot = elements[end]
    pi = start
    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, pi, elements)
            pi += 1
    swap(pi, end, elements)
    return pi


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)  # after finding the middle element we store that at pi index in the Array
        quick_sort(elements, start, pi - 1)  # in the 0 to pi-1 array & pi +1 to end array, we will again find
        quick_sort(elements, pi + 1, end)  # partition index(pi) and divide these arrays further till one element
        # remains which is implicitly sorted


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
