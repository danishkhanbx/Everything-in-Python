# Constructor is responsible for creating and assigning size to the Object
# Constructor calls init method to implicitly to define the size of the Object
class Computer:
    def __init__(self):
        self.name = 'Danish'
        self.age = 19

    def update(self):  # this self in update() function will take the object itself as a parameter
        self.age = 56

    def compare(self, other):  # self = c1 & other = c2
        if self.age == other.age:
            print("They are same")
        else:
            print("They are not same")


c1 = Computer()  # constructing an object c1 using Computer() constructor
c2 = Computer()

c1.name = 'Robert'
c1.age = 44
c1.update()  # means update(self -> c1)

print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):   # compare(self = c1, c2)
    pass
