import sys


def greet():  # recursion has a limit of 1000, it will stop after executing 1000 times.
    print("Hello")  # It is set up to stop infinite recursion, tough we can change the limit to some finite number
    greet()


print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
#greet()
print(sys.getrecursionlimit())
