from tkinter import *
# To show an image in tkinter we need to put the image inside a label and print that label inside the frame

root = Tk()
root.geometry('1065x437')

# png: supported in tkinter
# pic = PhotoImage(file='Img2.png')
# piclabel = Label(image=pic)
# piclabel.pack()

# jpg: not supported in tkinter GUI
# If we need to work with other file formats (example: .jpg), the Python Imaging Library (PIL) contains classes
# that let you load images in over 30 formats and convert them to GUI Tkinter-compatible image objects.
from PIL import Image, ImageTk
jpg = Image.open('Img2copy.jpg')
png = ImageTk.PhotoImage(jpg)  # ImageTk.PhotoImage will convert the image type to the type which is supported(png)
imglabel = Label(image=png)
imglabel.pack()

root.mainloop()
