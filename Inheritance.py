# A Subclass can access all the features of Super Class, but a Super class can not access any features of Subclass

## Single Level Inheritance
"""
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


a = A()
a.feature1()
a.feature2()

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()
"""


## MultiLevel Inheritance
"""
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(B):
    def feature5(self):
        print("Feature 5 working")


a = A()
a.feature1()
a.feature2()

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
"""


## Multiple Inheritance

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def feature5(self):
        print("Feature 5 working")


a = A()
a.feature1()
a.feature2()

b = B()
b.feature3()
b.feature4()

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
