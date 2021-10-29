import tkinter
import tkinter.messagebox

window = tkinter.Tk()

window.geometry("300x300")

def displayMsg():
    tkinter.messagebox.showinfo("Hello Python", "hello world")

button1 = tkinter.Button(window, text="Start", bg="lightgreen", command=displayMsg)
button1.pack(side='top', expand=tkinter.YES)

window.mainloop()