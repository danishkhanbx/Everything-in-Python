# Python program to count all duplicates from string using hashing
# Fills count array with frequency of characters
def fillCharCounts(string, count):
    for i in string:
        # at the index of the character which we will find using ord(i) we will increment value of char i from string
        # ord(i) will give the ASCII value of the character present in the 256 characters array count
        count[ord(i)] += 1
    return count


# Print duplicates present in the passed string
def printDups(string):
    count = [0] * NO_OF_CHARS  # Create an array of size 256 and fill count of every character in it
    count = fillCharCounts(string, count)

    k = 0  # Utility Variable: this will keep count of the number of iteration performed, current index = character

    # Print characters having count more than 0
    for i in count:  # it will iterate all the 256 indexes in the count array
        if int(i) > 1:
            print(chr(k) + ": count = " + str(i))
        k += 1  # to go to the next index = the next character


# Drivers program
NO_OF_CHARS = 256
string = "test string"
print(printDups(string))
