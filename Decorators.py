# without decorators
def div(a, b):  # when we always want nominator bigger than denominator
    if a < b:
        a, b = b, a
    print(a / b)


div(2, 4)


# Decorators are used to change the behavior of the existing function at compile time itself.
# we use decorators when we don't want to or can't access the function
def division(a, b):
    print(a / b)


def smart_div(func):  # taking function as a parameter
    def inner(a, b):  # defining function for swapping
        if a < b:
            a, b = b, a
        return func(a, b)  # it will return a,b after swapping if needed or not to division(a,b)

    return inner  # exiting inner after work is done


div1 = smart_div(division)  # building connection between div1 -> smart_div(division) -> division(swapped values)
div1(2, 4)  # or we can call using old division which will be updated to smart division i.e. division() & division=sd(d)
