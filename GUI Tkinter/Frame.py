from tkinter import *

root = Tk()
root.geometry('700x500')
root.title('Frames')

# Frame widget is a rectangular region on the screen that can be used as foundation class to implement complex widgets.
# This widget is very important for the process of grouping and organizing other widgets in a friendly way.
# It works like a container, which is responsible for arranging the position of other widgets.
# We can use bg, relief, borderwidth, bd as the attributes of the Frame. Some important attributes are discussed below:
# 1. bg: The normal background color displayed behind the label and indicator.
# 2. relief: The type of the border of the frame. Its default value is set to FLAT.
#            We can set it to any other styles, i.e., FLAT, RAISED, SUNKEN, GROOVE, RIDGE.
# 3. borderwidth: TkinterLabel doesn't have any border by default. We need to assign the borderwidth option to add a
#          border around the Label widget along with the relief option to be an option rather than flat to make visible.
# 4. bd: The size of the border around the indicator. Default is 2 pixels.

f = Frame(root, bg='grey', borderwidth=5, relief=SUNKEN)
f.pack(side=LEFT, fill='y')
f1 = Frame(root, bg='grey', borderwidth=5, relief=SUNKEN)
f1.pack(side=TOP, fill='x')

l = Label(f, text='Frame in GUI Tkinter')
l.pack(pady=142)
l1 = Label(f1, text='Welcome to Frame')
l1.pack()

root.mainloop()