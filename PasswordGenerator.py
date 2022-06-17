from tkinter import *
from tkinter import messagebox
import random

app = Tk()
app.geometry("400x300")

def check(length):
    if  length>0:
        create(length)
    else:
        messagebox.showerror("ERROR", "Please provide an integer greater than 0" )

def create(length):

    password = ""
    p.grid_forget()

    active = [] 

    for lst, value in zip(LISTS, values):
        if value.get() == True:
            active+=lst

    for _ in range(int(length)):
        password += active[random.randrange(len(active))]

    p.config(text = password)
    p.grid()

low, high, nums, misc = BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()

values = [low, high, nums, misc]

Low = [chr(i) for i in range(97,123)]
High = [chr(i) for i in range(65,91)]
Nums = [str(i) for i in range(10)]
Misc = ["!","@","#","$","*"]

LISTS = [Low,High,Nums,Misc]

Checkbutton(app, text = "a-z", variable = low, onvalue = True, offvalue = False ).grid(sticky = W, padx = 20)
Checkbutton(app, text = "A-Z", variable = high, onvalue = True, offvalue = False ).grid(sticky = W, padx = 20)
Checkbutton(app, text = "0-9", variable = nums, onvalue = True, offvalue = False ).grid(sticky = W, padx = 20)
Checkbutton(app, text = "!@#$*", variable = misc, onvalue = True, offvalue = False ).grid(sticky = W, padx = 20)

Label(app, text = "Enter password length:").grid(sticky = W, row = 0, padx = 150)
e =Entry(app)
e.grid(sticky = W, row = 1, padx = 150)

Button(app, text = "Confirm", command = lambda: check(int(e.get()))).grid(padx = 170,pady = 10)

Label(app, text= "Your new password is: ").grid()
p = Label(app, text = "", font = ("lucida", 16))
p.grid()

app.mainloop()