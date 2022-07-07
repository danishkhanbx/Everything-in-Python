# Types of Methods: Instance Method, Class Method, Static Method
# Instance Method works with instance variable using self keywords. 2 types of instance Accessor method & Mutator method
# Class Method works with class variable. We use cls keyword when working with class method.
# Static Method works with nothing. Used when we don't want to work with class & instance variables.
class Student:
    School = 'Angel High'  # Class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1  # Instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # Accessor method of Instance
        return self.m1

    def set_m1(self, value):  # Mutator method of Instance
        self.m1 = value

    @classmethod     # We use special symbol(Decorator) to use methods as a class method
    def getSchool(cls):
        return cls.School

    @staticmethod
    def info():
        print("Angel High is a High School")


s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.m1)  # when ae are only fetching the values we use Accessor method of Instance method
print(s1.get_m1())  # getter only fetch the value that's why they are called as Accessor
s1.set_m1(99)  # when we what to modify the values we use mutators using methods
print(s1.m1)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
