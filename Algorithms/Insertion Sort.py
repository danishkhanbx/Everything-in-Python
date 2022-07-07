# To sort an array of size N in ascending order:
# Iterate from arr[1] to arr[N] over the array.
# Compare the current element (key) index i to its predecessor index j = i-1.
# If the key element is smaller than its predecessor, compare it to the elements before j= i-2.
# Store the first value(assuming it is the smallest) in temp and move the greater elements one position ahead.

def sort(elements):
    for i in range(len(elements)):  # at i=0 nothing will work, so lets take i=2 and j=1
        small = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > small:  # j index greater than -1 and index j=1 element > index i=2 element
            elements[j + 1] = elements[j]      # storing j(1) value at j+1 = i = 2
            j = j - 1  # j=0 now, so on the next iteration the while loop will check if j=0 > i or not, if it is then
            # the swapping continues i.e. storing j value at j+1 = 1 until while one of conditions fails
        elements[j + 1] = small  # while loop exists at j=-1, so at index 0 storing the smallest element


if __name__ == '__main__':
    elements = [99, 77, 66, 88, 33, 22, 11, 0]
    sort(elements)
    print(elements)

