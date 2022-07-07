"""
# read
f = open('data', 'r')
# print(f.read()) # to read everything from the file
# print(f.readline(), end='')  # to read one line at a time from the file
# print(f.readline())
print(f.readline(4))  # will print only the first 4 characters from the file
for data in f:  # it will fetch everything one by one and print it
    print(data)
"""

"""
# write: to create a new file and write in it
f = open('abc', 'w')  # it will first check do we have a file named data, if we don't it will create the file
f.write("Hello ")  # when file is empty, we use write method
f.write("Mates ")
"""

"""
# append: when we don't want to lose the previous data present in the file
f = open('abc', 'a')
f.write('Hola Senor')

for abc in f:
    print(abc)
"""

"""
# copying the text in abc overwriting its own text from data
f = open('data', 'r')
f1 = open('abc', 'w')
for data in f:
    f1.write(data)
"""

# copying an image
f = open('img1.jpg', 'rb')   # reading byte code
# for i in f:
#     print(i)

f1 = open('Imgcopy.jpg', 'wb')  # opening a new file Imgcopy, then reading the byte code from f then
for i in f:  # writing it in the f1 file. So when we open the f1 file it shows an image. The byte code which was read
    f1.write(i)  # and wrote is now transformed into an img.
