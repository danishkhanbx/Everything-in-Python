x = 10  # Global variables
b = 9
print("Global variable b:", b, id(b))


def inside():
    global x  # explicitly making x global variable, so when we declare x=8 it will overwrite x=10
    x = 8
    print("in a function x:", x)

    b = 5  # local variable
    y = globals()['b']    # fetching global variable b into y, y is a local variable
    print("Local variable y:", y, id(y))       # now y will point to the address location where 9 is stored
    print("in a function b:", b)
    globals()['b'] = 876  # changing global variable b without affecting local variable b


inside()
print("Outside the function x:", x)
print("Outside the function b:", b)
