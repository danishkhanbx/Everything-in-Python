def sort(arr):
    size = len(arr)  # let size = 10 then the gap we go from 5, 2(floor value), 1
    gap = size // 2  # at gap of 1 this algorithm will work same as Insertion sort

    while gap > 0:
        for i in range(gap, size):  # when gap=5, picking elements in array by the gap number for current i, i.e. i=0,5
            anchor = arr[i]  # at i=0 the while loop will not start till i(5)=j i.e. gap=5 and j should be 5 or greater
            j = i            # when i=5, anchor[5] = 9 will be compared with index(0) = 11
            while j >= gap and arr[j - gap] > anchor:  # when j(5)>=5 & arr[5-5=0](11) > anchor(9), swap
                arr[j] = arr[j - gap]                  # arr[5] = arr[0](11)
                j -= gap                               # j=0 and while exists
            arr[j] = anchor                            # at arr[0]= anchor(9)
        gap = gap // 2  # now gap will be 2, so i=0,2,4,6,8 will be compared, starting with anchor(2)=7 and j=2
        # first 0,2 will be compared then 0,2,6 then 0,2,6,8, @ gap=1 every element will be compared like Insertion sort


if __name__ == '__main__':
    arr = [11, 13, 7, 12, 16, 9, 24, 5, 10, 3]
    sort(arr)
    print(arr)
