# Basic Function
"""
def greet():  # defining the function greet()
    print("Hello")


greet()  # calling it, so it will print the values in the function
"""


## Parameters(arguments) in function ##

# return void
def add(x, y):  # FORMAL ARGUMENT 
    z = x + y
    print(z)


add(5, 6)  # ACTUAL ARGUMENT 


# returning two parameters
def add_sub(a, b):
    c = a + b
    d = a - b
    return c, d


result1, result2 = add_sub(5, 4)
print(result1, result2)

# Until passed value is updated it works as a pass by value, after it is updated its address changes
print("No pass by value & pass by reference available in python")


def update(x):
    print("id x before: ", id(x))
    x = 8
    print("id x after: ", id(x))
    print("x: ", x)


a = 10
print("id a before: ", id(a))
update(a)
print("a: ", a)
print("id a after: ", id(a))

# Passing a list
print("Finding how many even and odd numbers of elements exist in a list")


def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count(lst)
print("Even: {} and Odd: {}".format(even, odd))

"""
# Actual Arguments #

# Position
def person(name, age):
    print(name)
    print(age)


person(19, "Danish")  # when we are not performing any operations on the argument, positions difference will work


# Keyword
def pal(name, age):
    print(name)
    print(age - 5)


# when we forget the position in which we have to pass the arguments and perform some operations on parameters
# then we use keywords i.e. age= , name=''. So it will assign name to the name & age to age argument in formal argument
pal(age=19, name='Khan')


# Default
def profile(name, age=18):  # in an account by default age should be 18 or greater, but if we pass a value it will
    print(name)  # override the existing value(18) with the new passed value
    print(age)


profile("danishkhanbx")  # when we are not passing a needed argument


# Variable Length
def sumof(a, *b):  # in this the number of arguments are not fixed
    print(a)  # we can also pass sumof(*b) means everything as a tuple
    print(b)
    c = a
    for i in b:
        c = c + i

    print(c)


sumof(5, 6, 34, 57)  # 5 will assign to a & 6,34,57,.. will be assigned to b as a tuple()


# Keyword Variable Argument or **kwargs
def info(name, **data):  # ** means passing multiple arguments with the help of keywords
    print(name)  # * means passing multiple arguments
    print(data)  # or for i,j in data.items(): # print(i, j)


info("Danish", age=19, city='Mumbai', mobile=9402385413)
"""
