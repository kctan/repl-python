import tkinter
import tkinter.messagebox

window = tkinter.Tk()

window.geometry("300x300")


button1 = tkinter.Button(window, text="Start", bg="lightgreen")
button1.config(font=("Courier", 30))
button1.pack(side='top', expand=tkinter.YES)

window.mainloop()