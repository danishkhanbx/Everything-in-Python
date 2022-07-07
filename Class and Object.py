# every time we create an Object it will take a new space.
# Size of Object = number of variables in it and size of each variable(different data types)
class Computer:
    def config(self):
        print("i5, 16GB, 1TB")


com1 = Computer()  # making com1 an Object of Computer using Computer() constructor
com2 = Computer()

Computer.config(com1)  # method config is inside class Computer for object com1
Computer.config(com2)

com1.config()  # com1 belongs to Computer so config belongs to Computer, behind the scene
com2.config()  # config will take com1 & com2 as a parameter
