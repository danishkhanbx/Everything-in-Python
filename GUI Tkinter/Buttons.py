from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Buttons')


def hello():
    print('Hello')


def how():
    print('How are you?')


def yo():
    print('Yo')


def up():
    print('Whats up')


f = Frame(root, bg='grey', borderwidth=5, relief=SUNKEN)
f.pack(side=LEFT, anchor='nw')

# A Python function or method can be associated with a button. This function or method will be executed if the button
# is pressed in some way. We can use bd, bg, command, fg, text, image, relief, etc., as attributes of the Button widget.
# 1. bg: The normal background color displayed behind the label and indicator.
# 2. relief: The type of the border of the frame. Its default value is set to FLAT. We can set it to any other styles.
# 3. bd: The size of the border in pixels. Default is 2 pixels.
# 4. font: Text font to be used for the button’s label.
# 5. image: Instead of text, Image to be displayed on the button.
# 6. command: Function or method to be called when the button is clicked. If the function is x(), we write command=x.

b = Button(f, fg='red', text='Hello', command=hello)
b.pack(side=LEFT, padx=42)

b1 = Button(f, fg='red', text='How are you?', command=how)
b1.pack(side=LEFT, padx=42)

b2 = Button(f, fg='red', text='Yo', command=yo)
b2.pack(side=LEFT, padx=42)

b3 = Button(f, fg='red', text='Whats up', command=up)
b3.pack(side=LEFT, padx=42)

root.mainloop()
