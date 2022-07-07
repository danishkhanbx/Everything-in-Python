from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('600x400')
root.title('Message Box')


# Python GUI Tkinter-MessageBox module is used to display the message boxes in the python applications.
# This module provides a number of functions that a user can use to display an appropriate message.
# Some of these functions are showinfo, askquestion, showwarning, showerror, askokcancel, askyesno, and askretrycancel.
# Parameters:
# Syntax: tkinter.messagebox.Function_Name(title, message, [options])
# tmsg is used to defining TKMessageBox. For this, we have to import tkinter.messagebox as tmsg.
# Function_Name: This is the name of the appropriate message box function.
# title: This is the text to be displayed in the title bar of a message box.
# message: This is the text to be displayed as a message in the message box.
# options: Options are alternative choices that may be used to tailor a standard message box.
# default: The default option is used to specify the default button, such as ABORT, RETRY,or IGNORE, in the message box.
# parent: The parent option is used to specify the window on top of which the message box is to be displayed.
def help():
    print('We will help you')
    tmsg.showinfo('Help', "Don't worry we will help you from our side.")


def rate():
    print('Rate us')
    value = tmsg.askquestion('Experience', 'Was your experience good?')
    print(value)
    if value == 'yes':
        msg = 'Great. Rate us on appstore please!'
    else:
        msg = 'Tell us what went wrong! We will resolve it soon.'
    tmsg.showinfo('Feedback', msg)


def hack():
    ans = tmsg.askretrycancel('Hack', 'Currently unable to hack, retry sometime later.')
    if ans:
        print('Sorry we are not able to hack it.')
    else:
        print('Good you cancel it, we will never be able to hack Google, goto sleep kid.')


mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='Help', command=help)
m1.add_command(label='Rate us', command=rate)
m1.add_command(label='Hack Google', command=hack)
mainmenu.add_cascade(label='Help', menu=m1)

root.config(menu=mainmenu)
root.mainloop()
