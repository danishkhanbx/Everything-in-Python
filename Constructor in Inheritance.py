"""
# When we create object of Subclass it will call init of Subclass first, if we had called super then it will first call
# init of Super class then call init of Subclass. We can also use super().x method to call another method i.e. method x.
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__()  # when init of B is called, it will call its parent init method
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


a = B()  # creating 'a' object using Constructor B, it will print init in B if init in B exist or init of A if it exists
"""


# Method Resolution Order(MRO): moves from left to right
# eg: when we call super().init in C(A,B) it will call left parent(A) first & print in A init,
# if called again then it will print the right parent(B) and print in B init.
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1A working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature 1B working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()  # now which init it will call, it called init of A because of MRO
        print("in C init")


a = C()
a.feature1()  # calling the same method which exist in both class A & B, to check which one will print respect to MRO
