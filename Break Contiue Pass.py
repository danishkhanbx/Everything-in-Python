# The break statement, breaks out of the innermost enclosing for or while loop.
# Loop statements may have an else clause; it is executed when the loop terminates.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# The continue statement, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# pass does nothing. It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


class MyEmptyClass:
    pass


def initlog(*args):
    pass  # Remember to implement this!
