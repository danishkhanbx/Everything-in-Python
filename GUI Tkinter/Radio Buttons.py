from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Radiobutton')


def submit():
    print(f'{var.get()} submitted')


# Radiobutton() widget is a graphical user interface element of GUI Tkinter, which allows the user to choose (exactly) one
# of a predefined set of options. Sometimes it is called the options button. Radiobuttons can contain text or images.
# The button can only display text in a single font. A Python function or method can be associated with a radio button.
# This function or method will be called if you press this radio button.
# In order to implement this functionality, each group of radiobuttons must be associated with the same variable (we
# have to initialize the variable firstly if it is StringVar()) & each one of the buttons must symbolize a single value.
# You can use the Tab key to switch from one radionbutton to another.
# Attributes:
# anchor: If the widget inhabits a space larger than it needs, this option specifies where the radiobutton will sit
#         in that space (i.e. e, w). The default is anchor=CENTER.
# justify: If the text contains multiple lines, this option controls how the text is justified: CENTER(default), R, & L.
# value: When a radiobutton is turned on by the user, its control variable is set to its current value option.
#        If the control variable is an IntVar, give each radiobutton in the group a different integer value option.
#        If the control variable is a StringVar, give each radiobutton a different string value option.
# variable: The control variable that this radiobutton shares with the other radiobuttons in the group.
#           This can be either an IntVar() or a StringVar(). If it is StringVar() it should be initialized beforehand
#           with some other string variable name using the set() function.
# bg: It shows the normal background color behind the indicator and label.
# font: It is used to set the font used for the text.
# text: It is the label displayed next to the radiobutton. Use newlines ("\n") to display multiple lines of text.
var = StringVar()
var.set("Radio")
Label(root, text='Select the following', font='lucida 10 bold', justify=LEFT, padx=14).pack()
Radiobutton(root, text='A', padx=14, variable=var, value='A').pack(anchor='w')
Radiobutton(root, text='B', padx=14, variable=var, value='B').pack(anchor='w')
Radiobutton(root, text='C', padx=14, variable=var, value='C').pack(anchor='w')
Radiobutton(root, text='D', padx=14, variable=var, value='D').pack(anchor='w')

Button(text='Submit', command=submit).pack()

root.mainloop()
