# __init__ is a Special Method
# init stands for initializing variables, and it will be called implicitly.
# The functions inside init will always get printed object times means the number of objects in the file = init printed
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu  # to object(self) values are getting assigned
        self.ram = ram

    def config(self):  # fetching the values using self->object->com1 | com2 and printing them
        print("Config:", self.cpu, self.ram, "GB")


com1 = Computer('i5', 16)   # passing arguments within constructor (com1->object,x,y) is getting past
com2 = Computer('Ryzen3', 8)

com1.config()
com2.config()
