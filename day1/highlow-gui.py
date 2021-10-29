from tkinter import *
import random

def calculate():
    global low, high
    user_guess = int(e1.get())
    if user_guess > secret:
        high = user_guess
        l1.config(text="Too High")
    elif user_guess < secret:
        low = user_guess
        l1.config(text="Too Low")
    else:
        l1.config(text="You have guessed correctly!")
    
    hint = "Enter a number between " + str(low) + " and " + str(high)
    l2.config(text=hint)

secret = random.randint(1, 99)
print("secret: " + str(secret))

low = 1
high = 99

master = Tk()
master.geometry("300x300")

l1 = Label(master, text="Start Game")
l2 = Label(master, text="Enter a number between 1 and 99")
l1.grid(row=0, column=0)
l2.grid(row=1, column =0)

e1 = Entry(master)
e1.grid(row=2, column=0)

Button(master, text='Guess',command=calculate).grid(row=3, column=0)

mainloop( )

