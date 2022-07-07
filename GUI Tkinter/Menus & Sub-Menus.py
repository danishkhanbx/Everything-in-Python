from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Menus and Submenus')


def func():
    print('XYz')


# The Menu widget is used to implement different types of menus (toplevel, pulldown, and popup menus).
# The goal of this widget is to allow us to create all kinds of menus that can be used by our applications.
# It is also possible to use other extended widgets to implement new types of menus, such as the OptionMenu widget,
# which implements a special type that generates a pop-up list of items within a selection.
# Attributes:
# bg: The background color for choices not under the mouse.
# bd: The width of the border around all the choices. Default is 1.
# fg: The foreground color used for choices not under the mouse.
# tearoff: Normally, a menu can be torn off. The first position (position 0) in the list of choices is occupied by
#          the tear-off element and the additional choices are added starting at position 1. If you set tearoff=0,
#          the menu will not have a tear-off feature and choices will be added starting at position 0.
# relief: The default 3-D effect for menus is relief=RAISED.
# title: Normally, the title of a tear-off menu window will be the same as the text of the menubutton or cascade
#        that lead to this menu. If you want to change the title of that window, set the title option to that string.

# For creating a non-dropdown menu widget:
# Menu() widget is created in the root or parent window and this widget is taken as a variable named "mymenu".
# For adding a menu item to the Menu widget we use add_command() method. We pass the attribute "label" which shows the
# name of the given menu item (i.e. "File", "Exit") and command which call the function and executes the statement
# within the function (i.e. myfunc, quit).
# config() is used to access an object's attributes after its initialization and then the menu is set with the variable
"""
mymenu = Menu(root)
mymenu.add_command(label='File', command=func)
mymenu.add_command(label='Exit', command=quit)
root.config(menu=mymenu)
"""
# For creating a dropdown menu widget:
# Menu() widget is created in the root or parent window and this widget is taken as a variable named "mainmenu".
# Two dropdown menus are created (m1 & m2). With each menu, four menu items are added and their names are set using the
# Label attribute (i.e. New Project, Save, Print, etc.) Tearoff=0 is used so that the menu will not have a tear-off
# feature, and choices will be added starting at position 0 (the menu section will be attached with GUI window always).
# config() is used to access an object's attributes after its initialization and then the menu is set with the variable.
# For adding the new hierarchical menu by associating a given menu m1 to a parent menu mainmenu add_cascade() is used
# and the label is passed to set the name of the label (i.e. "File").
# For adding a separator line to the menu we use add_separator() method.
mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='New Project', command=func)
m1.add_separator()
m1.add_command(label='Save', command=func)
m1.add_command(label='Save as', command=func)
m1.add_command(label='Print', command=func)
mainmenu.add_cascade(label='File', menu=m1)

m2 = Menu(mainmenu)
m2.add_command(label='Copy', command=func)
m2.add_command(label='Cut', command=func)
m2.add_command(label='Paste', command=func)
m2.add_separator()
m2.add_command(label='Find', command=func)
mainmenu.add_cascade(label='Edit', menu=m2)

root.config(menu=mainmenu)
root.mainloop()
