from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Scroll Bar')

# The Scrollbar() widget provides a slide controller used to implement vertically scrolled widgets, such as Listbox,
# Text, and Canvas. Horizontal scrollbars can also be used with the Entry widget.
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# To connect a vertical scrollbar to such a widget, you have to do two things:
# Set the widget’s yscrollcommand callbacks to the set method of the Scrollbar.
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(300):
    listbox.insert(END, f'Item {i}')
listbox.pack()
# Set the Scrollbar’s command to the yview method of the widget using config().
scrollbar.config(command=listbox.yview)

# Attributes:
# bg: It is used to set the color of the slider and arrowheads when the mouse is not over them.
# bd: The width of the 3-d borders around the trough’s entire perimeter and the width of the 3-d affects the arrowheads
# and slider. Default is no border around the trough and a 2-pixel border around the arrowheads and slider.
# orient: It is used to set orient=HORIZONTAL for a horizontal scrollbar, orient=VERTICAL for a vertical one.
# width: It sets the width of the Scrollbar (its y dimension if horizontal, & its x dimension if vertical). Default 16.

root.mainloop()
