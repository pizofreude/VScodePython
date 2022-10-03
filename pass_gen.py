# Password Generator Python Project.
"""
Project File Structure.
Step to build a Password Generator using Python:

1. Import modules.
2. Initialized Window.
3. Select Password Length.
4. Function to Generate Password.
5. Function to Copy Password.
6. Loop to run program.
"""

# 1. Import Libraries.
from tkinter import *
import random
import string
import pyperclip

# 2. Initialize Window.
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Pizofreude - COMPLEX PASSWORD GENERATOR")
# Label() widget use to display one or more than one line of text that users can’t able to modify.
Label(root, text = 'COMPLEX PASSWORD GENERATOR' , font ='arialBLACK 15 bold').pack()
Label(root, text ='Pizofreude', font ='arial 15 bold').pack(side = BOTTOM)

# 3. Select Password Length.
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()  
pass_len = IntVar()  # IntVar: Integer type variable that stores the length of a password.
# Spinbox() widget is used to select from a fixed number of values. Here the value from 8 to 32.
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()  

# 4. Function to Generate Password.
pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

# 5. Function to Copy Password.
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)



# 6. Loop to run program.
root.mainloop()
