from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Entry & Grid')


def Input():
    print(f'My name is {name.get()}')
    print(f'My age is {age.get()}')


## Grid Layout
# This geometry manager organizes widgets in a table-like structure in the parent widget.
# Syntax: widget.grid( grid_options )
# column: The column to put widget in; default 0 (leftmost column).
# columnspan: How many columns widgetoccupies; default 1.
# ipadx, ipady: How many pixels to pad widget, horizontally and vertically, inside widget's borders.
# padx, pady: How many pixels to pad widget, horizontally and vertically, outside v's borders.
# row: The row to put widget in; default the first row that is still empty.
# rowspan: How many rowswidget occupies; default 1.
# sticky: What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell.
# Sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions
# indicating the sides and corners of the cell to which widget sticks.
Label(root, text='Enter your Name').grid(row=0, column=0)
Label(root, text='Whats yur age').grid(row=1, column=0)

## Text Input
# The Entry Widget is a GUI Tkinter Widget used to Enter or display a single line of text.
# Syntax: entry = tk.Entry(parent, options)

# Parameters:
# 1) Parent: The Parent window or frame in which the widget to display.
# 2) Options: The various options provided by the entry widget are:
# bg : The normal background color displayed behind the label and indicator.
# bd : The size of the border around the indicator. Default is 2 pixels.
# font : The font used for the text.
# fg : The color used to render the text.
# justify : If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT.
# relief : With the default value, relief=FLAT. You may set this option to any of the other styles.
# show : Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each
# character as an asterisk, set show=”*”.
# textvariable: In order to be able to retrieve the current text from your entry widget, you must set this option to an
# instance of the StringVar class.

# Methods: The various methods provided by the entry widget are:
# get(): Returns the entry’s current text as a string.
# delete(): Deletes characters from the widget
# insert(index, ‘name’): Inserts string ‘name’ before the character at the given index.
name = Entry(root, width=50, borderwidth=5)
name.grid(row=0, column=1)
age = Entry(root, width=50, borderwidth=5)
age.grid(row=1, column=1)

Button(root, fg='red', text='Submit', command=Input).grid(row=3, column=1)

root.mainloop()
