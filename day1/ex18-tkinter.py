from tkinter import *

def show_entry_fields():
    total = int(e1.get()) + int(e2.get())
    resultText = "Sum of 2 numbers: " + str(total)
    resultLabel.config(text=resultText)
   

master = Tk()
master.geometry("300x300")
Label(master, text="First Number").grid(row=0)
Label(master, text="Second Number").grid(row=1)

resultLabel = Label(master, text="Answer: ")
resultLabel.grid(row=4)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Calculate', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
