# Polymorphism(One thing Many Forms): Duck Typing, Operator Overloading, Method Overloading & Method Overriding

# Method Overloading: in some case we are passing 1 argument, 2 arguments, 3 args we need to create 3 different methods
# with different number of parameters' intake, all 3 will perform the same operation of summing of all parameters passed
# So, we create a general purpose method which performs different operations and load different answers with different
# when number of parameters are passed is called Method Overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None,
            c=None):  # when 1 arg is passed b & c will be null and only a will pe summed up with
        s = 0  # s and returned, when 2 args is passed c will be null then a & b will be
        if a != None and b != None and c != None:  # be summed up with s and returned, when 3 args is passed then a,b &
            s = a + b + c  # c will be summed up and returned
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(58, 69)
print(s1.sum(5, 5, 5))
print(s1.sum(1, 1))
print(s1.sum(4))


# Method Overriding
class A:
    def show(self):
        print('in A show')


class B(A):
    def show(self):  # or pass then it will go in the parent method and search show method and print in A show
        print('in B show')


a = A()
a.show()
a = B()  # child's method will override parents method
a.show()
