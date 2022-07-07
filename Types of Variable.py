# Instance variable are different for different objects
# i.e. When we change variable of one object it does not affect other objects.
# Class variable will be same for all the objects in the same class.
# i.e. When we change variable of a Class variable it will affect all the objects in the same class.
# In our memory we have different namespace( is an area where we create and store object/variable). 2 types of namespace
# Class namespace where we stored all the class variable. Instance namespace to create & store object/instance.
# Class and Static are the same in Variables.
class Car:
    wheels = 4   # Class variable & it belongs to Class namespace

    def __init__(self):
        self.mil = 10    # Instance variable mil & com because it will change with object
        self.com = 'BMW' # Instance namespace


c1 = Car()
c2 = Car()

c1.mil = 8      # Instance variable mil got changed. It can be accessed using object only
Car.wheels = 2  # Class variable can be accessed using class or object(i.e. c1.wheels)

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
