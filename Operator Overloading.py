# Polymorphism(One thing Many Forms): Duck Typing, Operator Overloading, Method Overloading & Method Overriding
# 5 + 6: 5 & 6 are Operands and + is an Operator
# The moment we call the Operands it calls the magic methods(__add__,__str__,...) which works behind the operands
a = 5
b = 7
print(a + b)
print(int.__add__(a, b))  # this is what happening behind on above a+b, add is the method which belongs to the int class

c = '5'
d = '9'
print(str.__add__(c, d))


# Operator Overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # overloading + operator, restructuring add method to add 2 objects into one & return it
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        s3 = Student(m1, m2)  # creating an initializing object of s3 with values m1 & m2
        return s3

    def __gt__(self, other):  # overloading > operator
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            print("s1 wins")
        else:
            print("s2 wins")

    def __str__(self):  # s2 will print in str format, so wherever there is a one string present -> convert it to int
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2  # s1 and s2 are two objects to add objects we need to create a method, Student.__add__(s1,s2)
print('s3:', s3)

if s1 > s2:  # > operator is getting restructured in __gt__ method
    pass

print('s2:', s2)  # changing from object address in string to int values
