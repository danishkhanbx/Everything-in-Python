from tkinter import *

root = Tk()
root.geometry('644x334')
root.title('Events Handling')


# Event formats:
# <Button-1>: A mouse button is pressed over the widget. Button 1 is the leftmost button, Button 2 is the middle button
#             (where available), and Button 3 is the rightmost button.
# <B1-Motion>: The mouse is moved, with mouse button 1 being held down (use B2 for the middle button,
#              B3 for the right button).
# <Double-Button-1>: Button 1 was double-clicked. You can use Double or Triple as prefixes.
# Note: Both bindings will be called if you bind to both a single click (<Button-1>) and a double click.
# <Enter>: The mouse pointer entered the widget. Note: This event doesn't mean that the user pressed the Enter key.
# Event attributes: As Event attributes, we can use width, height, char, num, widget, etc.
def Input(event):
    print(f'You clicked on the button at {event.x}, {event.y}')


widget = Button(root, text='Submit')
widget.pack()
widget.bind('<Button-1>', Input)
widget.bind('<Double-1>', quit)

root.mainloop()
