from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Sliders')


# The Scale() widget provides a graphical slider object that allows the user to select numerical values by moving the
# “slider” knob along the specific scale. Users can control the minimum and maximum values as well as the resolution.
# Methods:
# get(): This method returns the current value of the scale.
# set(value): It sets the scale’s value. For example, if we give set(30) the initial scale value will show 30
# (the scale will start from 30).
def getlines():
    print(f'There are {slider1.get()} number of lines their in the code')


# Attributes:
# from_: This should be a float or integer value that defines one end or the starting value of the scale’s range.
# to: This should also be a float or integer value that defines the other end or the finishing value of the scale’s
#     range. Note: The to value can be either greater than or less than the from_ value. For vertical scales, the to
#     value defines the bottom of the scale; for horizontal scales, the right end.
# orient: It sets the orientation of the scale. If we set orient=HORIZONTAL, the scale runs along the x dimension, or we
#         set orient=VERTICAL, it runs parallel to the y-axis. Default is vertical.
# length: It sets the length of the Scale() widget. It defines the x dimension if the scale is horizontal or
#         the y dimension if vertical. The default value is 100 pixels.
# resolution: Normally, the user is only able to change the scale in whole units. But this attribute sets this option
#             to some other value to change the smallest increment of the scale’s value. For example, if from_=-10 and
#             to=10, and you set resolution=5, the scale will have 5 possible values: -10, -5, 0, +5, and +10.
# tickinterval: It displays periodic scale values. If we set this option to a number, ticks will be displayed on
#               multiples of that value. For example, if from_=0, to=10, and tickinterval=2, labels will be displayed
#               along the scale at values 0, 2, 4, 6, 8, 10. These labels appear below the scale if horizontal,
#               to its left if vertical. Default is 0, which suppresses the display of ticks.
slider1 = Scale(root, from_=0, to=200, tickinterval=5)
slider1.pack(fill=Y, side=RIGHT)
slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=3)
slider2.pack(fill=X, side=BOTTOM)

Label(root, text='How many lines in the code?').pack()
Button(root, text='Get Total Lines', pady=10, command=getlines).pack()

root.mainloop()
