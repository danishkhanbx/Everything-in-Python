from array import *


def findduplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                print(arr[i])
    # or
    """ Let say nums[ 1, 3, 2, 3 ]
    while nums[0] != nums[nums[0]]:   # i.e nums[0] (1) != nums[nums[0]] (nums[1] = 3), the index 0 will keep changing
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]  # so swap, we get nums[ 3, 1, 2, 3 ] nums[0] = 3 and nums[1] = 1
    return nums[0]   # now, nums[0] (3) == nums[nums[0]] (nums[3] = 3)
    """


arr = []
n = int(input("Enter number of elements: "))
for i in range(n + 1):
    x = int(input('Enter array elements: '))
    arr.append(x)
print(arr)
findduplicate(arr)
