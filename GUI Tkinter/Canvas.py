from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f'{canvas_width}x{canvas_height}')
root.title('Canvas')

# The Canvas() widget is a rectangular area for drawing pictures or other complex layouts. This is a highly versatile
# widget that can draw graphs and plots, create graphics editors, and implement various custom widgets.
# The canvas is a general-purpose widget, which is typically used to display and edit graphs and other drawings.
# Another common use for this widget is to implement various kinds of custom widgets.

# The most commonly used options for this widget(these options can be used as key-value pairs separated by commas):
# bd: It defines the border width in pixels. The default value is 2.
# bg and relief: Normal background color and It specifies the type of border.
# width, height: It defines the size of the canvas in the X and Y dimensions respectively.

can = Canvas(root, width=canvas_width, height=canvas_height)
can.pack()

# Here is the list of some standard items which the Canvas widget can support:
# arc: It creates an arc item which can be a chord, a pie slice, or a simple arc.
# line: It creates a line item.
can.create_line(0, 0, 800, 200, fill='red')  # start(x,y) to end(x,y)
can.create_line(0, 200, 800, 0, fill='red')
# oval: It creates a circle or an ellipse at the given coordinates. It takes two pairs of coordinates; the top left
#       and bottom right corners of the bounding rectangle for the oval.
can.create_oval(10, 30, 700, 300, fill='yellow')
# rectangle: It creates a rectangle at the given coordinates. It takes two pairs of coordinates; the top left corner
#            and the bottom right corner of the rectangle.
can.create_rectangle(10, 30, 700, 300)

can.create_text(350, 150, text='Canvas')


root.mainloop()