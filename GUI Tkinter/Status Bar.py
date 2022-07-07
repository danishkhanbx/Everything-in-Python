from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Status Bar')


def upload():
    statusbar.set('Busy..')
    sbar.update()
    import time
    time.sleep(2)
    statusbar.set('Ready now')


# A StringVar() is taken as “statusvar” (a string variable), and is set.
statusbar = StringVar()
statusbar.set('Ready')

# Inside the Label we will print the StringVar
sbar = Label(root, textvariable=statusbar, relief=SUNKEN, anchor='c')
sbar.pack(fill=X, side=BOTTOM)

Button(root, text='Upload', command=upload).pack()

root.mainloop()
