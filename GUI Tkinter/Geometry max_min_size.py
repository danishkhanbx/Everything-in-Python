from tkinter import *
# Geometry, Min ,and max size of the frame

root = Tk()

# Geometry(): This method is used to set the dimensions of the GUI Tkinter window and is used to set
# the position of the main window on the user’s desktop.
root.geometry('444x244')  # width x height, when started initialize size will be of geometry

# Minsize(): This method is used to set the minimum size of the GUI Tkinter window. Using this method user can set
# the window’s initialized size to its minimum size and still be able to maximize and scale the window larger.
root.minsize(200, 100)  # width, height, it cannot be minimized less than given width & height

# Maxsize(): This method is used to set the maximum size of the GUI Tkinter window, i.e., the maximum size of a window
# can be expanded. Users will still be able to shrink the size of the window to the minimum possible.
root.maxsize(800, 500)  # width, height, it cannot be maximized more than given width & height

root.mainloop()