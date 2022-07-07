from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('List Box')


# The Listbox() widget is a standard GUI Tkinter widget that displays a list of items from which a user can select a number
# of items. The Listbox can only contain text items, and all items must have the same font and color. Depending on the
# widget configuration, the user can choose one or more alternatives from the list.
# Listboxes are used to select from a group of textual items. Depending on how the Listbox is configured, the user can
# select one or many items from that list.
# Attributes:
# bg & fg: It is used to set the background color of the widget & color of the text respectively.
# bd: It represents the size of the border. The default value is 2 pixels.
# font: It sets the font type of the Listbox items (the font type of all Listbox items will be the same).
# Methods:
# activate(index): It is used to select the lines at the specified index.
# delete(first, last = None): It is used to delete the lines which exist in the given range.
# insert(index, *elements): used to insert the new lines with the specified number of elements before the specified indx
# get(first, last = None): It is used to get the list of items that exist in the given range.
# index(i): It is used to place the line with the specified index at the top of the widget.
def add():
    global i
    listbox.insert(END, f'{i} item')
    i += 1


i = 2
listbox = Listbox(root)
listbox.pack()
listbox.insert(END, 'First item')
Button(root, text='Add Item', command=add).pack()

root.mainloop()
