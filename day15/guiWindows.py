
"""
WIDGETS = gui elements, buttoms, textboxes, (attachments to windows)
    label = area of widget that holds text and//or an image
WINDOWS = container for widgets
"""
from tkinter import *
window = Tk()  # instantiate an instance of a window

"""WINDOW FEATURES
width = "300"
height = "300"
window.geometry(width, height)
window.title("My First GUI program")

logo = ""
icon = PhotoImage(file=logo)
window.iconphoto(True, icon)

window.config(
    background = "",
    )
"""


"""LABELS
labelText = "Hello World"
label = Label(
    window,
    text=labelText,
    font=('Arial', 40, 'bold'),
    fg='green',
    bg='black'
    relief=RAISED,
    bd=10
    padx=20
    pady=20)
#label.place(x=0,y=0)
label.pack() # by default will place widget in center 
"""


"""BUTTONS
count = 0
def click():
    global count
    count += 1
    print(count)

button = Button(window,
    text='click me',
    command=click,
    font=("Comic Sans", 30),
    fg="green",
    bg="black"
    activeforeground="green",
    activebackground="black")
button.pack()
"""


def submit():
    username = entry.get()
    print("hello "+username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get())-1, END)


# customize appearance
entry = Entry(
    window,
    font=('arial', 50),
    fg='green',
    bg='black',
)
entry.pack(side=LEFT)

# default text


submit_button = Button(window, text="submit", command="submit")
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command="delete")
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command="backspace")
backspace_button.pack(side=RIGHT)


window.mainloop()  # place window on computer screen and listne for events
