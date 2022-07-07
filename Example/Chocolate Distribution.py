def find_min_diff(arr, n, m):
    if m == 0 or n == 0:  # if there are no chocolates or number of students is 0
        return 0

    arr.sort()   # [2, 4, 7, 9, 12, 23, 25, 28, 30, 30, 40, 41, 42, 43, 44, 48, 50]

    if m > n:  # Number of students cannot be more than number of packets
        return -1

    min_diff = arr[n - 1] - arr[0]  # Largest difference between given number of chocolates, arr[16] - arr[0] = 50-2= 48

    for i in range(len(arr) - m + 1):  # if n=17 then arr[0..16] & m=7, so when i=10 then i+m-1=16, that's why len = 11
        if min_diff > arr[i + m - 1] - arr[i]:  # and arr[10+7-1] - arr[10] = 22, compare it with recorded min diff
            min_diff = arr[i + m - 1] - arr[i]

    return min_diff


if __name__ == '__main__':
    chocolate = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    n = len(chocolate)
    m = 7  # Number of students
    print('Minimum Difference is ', find_min_diff(chocolate, n, m))
