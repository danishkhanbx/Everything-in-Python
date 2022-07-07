from tkinter import *

root = Tk()

root.geometry('700x300')
root.title('Labels')

# Label(): A Label is a GUI Tkinter Widget class used to display text or an image.
# The label is a widget that the user just views but does not interact with.
# pack() method: It organizes the widgets in blocks before placing them in the parent widget.
"""
# Label & Pack
HelloWorld = Label(text='Hello, how are you?')
HelloWorld.pack()  # after we had added something inside the GUI tab, we need to pack the object inside the frame
"""

# Attributes of Label
# Attributes of Label: The Label widget is a standard GUI Tkinter widget used to display a text or image on the screen.
# There are a lot of attributes of the Label widget. Some important attributes are discussed below:
# 1. bg: The normal background color displayed behind the label and indicator.
# 2. fg: This option specifies the color of the text (foreground color). If you are displaying a bitmap,
#        this is the color that will appear at the position of the 1-bits in the bitmap.
# 3. padx: Extra space added to the left and right of the text within the widget. Default is 1.
# 4. pady: Extra space added above and below the text within the widget. Default is 1.
# 5. relief: Specifies the appearance of a decorative border around the label. There are five types of reliefs,
#            such that FLAT, RAISED, SUNKEN, GROOVE, RIDGE. The default is FLAT.
# 6. font: If you are displaying text in this label (with the text or text variable option),
#          the font option specifies the style, size, and other characteristics (i.e. bold, italic, etc.)
#          of the font, and in this style, the text will be displayed.
# 7. text: To display one or more lines of text in a label widget, set this option to a string containing the text.
#          Internal newlines (“\n”) will force a line break.
# 8. justify: Specifies how multiple lines of text will be aligned with respect to each other:
#             LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.
# 9. height: The vertical dimension of the new frame.
# 10. width: The horizontal dimension of the new frame.
#            If this option is not set, the label will be sized to fit its contents.

label = Label(text='''The Graphical user interface(GUI) is used by today's most commercially popular computer operating 
\nsystems and software programs. It's the kind of interface that allows users to manipulate elements on the screen using
\na mouse, a stylus, or even a finger.Widgets are the basic building blocks for graphical user interface (GUI) 
\napplications. Each GUI component (e.g., buttons, labels) is a widget that is placed somewhere within a user interface 
\nwindow or is displayed as an independent window. GUI Tkinter also offers access to the widgets' geometric configuration, 
\nwhich can organize the widgets in the parent windows. There are mainly three geometry manager classes.''',
              bg='grey', fg='white', padx='2', pady='2', font='comicsansms 10 italic', borderwidth=5, relief=SUNKEN)

# Attributes of Pack
# The Pack geometry manager packs widgets in rows or columns. We can use  options like fill, expand,
# and side to control this geometry manager.
# 1. fill: Determines whether widget fills any extra space allocated to it by the packer or keeps its own
#          minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically),
#          or BOTH (fill both horizontally and vertically).
# 2. side: Determines which side of the parent widget packs against TOP, BOTTOM, LEFT, or RIGHT. The default is TOP.
# 3. anchor: Anchors are used to define where text is positioned relative to a reference point.
#            The anchor attributes are: n, s, e, w, center, nw, sw, be, and se. The default is center.
label.pack(fill=X and Y, side=BOTTOM, anchor='se')

root.mainloop()
