# Polymorphism(One thing Many Forms): Duck Typing, Operator Overloading, Method Overloading & Method Overriding
class Myeditor:
    def execute(self):
        print('Compiling')
        print('Running')


class Pycharm:
    def execute(self):
        print('Spell check')
        print('Convention check')
        print('Compiling')
        print('Running')


class Laptop:
    def code(self, ide):  # code(Laptop, Myeditor)
        ide.execute()     # Myeditor.execute will run execute method in Myeditor class


ide = Myeditor()  # or Pycharm(), we can change the ide and the laptop should run the code
lap = Laptop()
lap.code(ide)  # lap -> Laptop().code(self, Myeditor) -> code(Laptop, Myeditor) -> Myeditor.execute() -> prints
