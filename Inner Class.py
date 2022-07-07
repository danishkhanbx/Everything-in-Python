# We create inner class when the inner class will only exist for the outer class
# We can create object of inner class inside the outer class. OR
# We can create object of inner class outside the outer class provided we use outer class name to call it
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()  # creating object of Laptop which is in inner class to access Laptop() -> lap
        # which is in outer class, so we can access values of Laptop outside the inner class using lap

    def show(self):
        print(self.name, self.roll)
        self.lap.show()  # accessing show method of Laptop class using lap object which is inside self object

    class Laptop:  # inner class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8GB'

        def show(self):
            print(self.brand, self.ram, self.cpu)


s1 = Student('Danish', 2)
s2 = Student('Khan', 76)
s1.show()

print(s1.lap.brand)  # accessing Laptop variables using lap of object s1

lap1 = s1.lap  # creating another object of lap1 using s1.lap = s1.Laptop()
lap2 = s1.lap
lap3 = Student.Laptop()

print(lap1.cpu)  # accessing Laptop variables using lap1 object
