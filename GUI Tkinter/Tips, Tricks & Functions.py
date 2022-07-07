from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Tips, Tricks and Functions')

# wm_iconbitmap: It is used to set the window icon. Here the icon "1.ico" will be shown as the window icon.
root.wm_iconbitmap('Img2.png')

# configure(): It is used to change the formatting of the GUI window. Here, we set the configuration passing
#              "background" attribute as grey to make the window in grey color.
root.configure(background='grey')

# winfo_screenwidth(): This is used to know the width of the current window.
# winfo_screenheight(): This is used to know the height of the current window.
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f'{width}x{height}')

# destroy: This method is used to destroy or close the particular GUI window. Here this method is used with a button.
#          So when the button "Close" is clicked, the GUI window will be closed.
Button(text='Close', command=root.destroy).pack()

root.mainloop()
