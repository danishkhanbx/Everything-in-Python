from tkinter import *
# Status Bar using OOPs


def click():
    print('Button clicked')


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('OOPs')

    def status(self):
        self.var = StringVar()
        self.var.set('Ready')
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor='c')
        self.statusbar.pack(side=BOTTOM, fill=X)

    def createbutton(self, inptext):
        Button(text=inptext, command=click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton('Click me')
    window.mainloop()
