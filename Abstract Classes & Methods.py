from abc import ABC, abstractmethod
# ABC = Abstract Base Class. Abstract class which has least one abstract method in the class.
# Abstract methods are which doesn't have any definition it only has a declaration.


class Computer(ABC):  # abstract class Computer which have abstract method process
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):  # cls Laptop is inheriting abstract cls Computer, so it is compulsory to define abstract method
    def process(self):
        print('its running')


#com = Computer()
#com.process()
com1 = Laptop()
com1.process()
