from tkinter import *
from backend import *

def add_book():
    insert(title_string.get(), author_string.get(), year_string.get(), isbn_string.get() )

window = Tk()

l1 = Label(window, text='title')
l1.grid(row=0, column=0)
title_string = StringVar()
e1 = Entry(window, textvariable=title_string)
e1.grid(row=0, column=1)

l2 = Label(window, text='author')
l2.grid(row=1, column=0)
author_string = StringVar()
e2 = Entry(window, textvariable=author_string)
e2.grid(row=1, column=1)

l3 = Label(window, text='year')
l3.grid(row=2, column=0)
year_string = StringVar()
e3 = Entry(window, textvariable=year_string)
e3.grid(row=2, column=1)

l4 = Label(window, text='isbn')
l4.grid(row=3, column=0)
isbn_string = StringVar()
e4 = Entry(window, textvariable=isbn_string)
e4.grid(row=3, column=1)

b1 = Button(window, text="insert Book", width=12, command= add_book)
b1.grid(row=0, column=4)




window.mainloop()
