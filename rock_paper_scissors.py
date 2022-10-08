# Python Rock Paper Scissors Game.
"""
Project File Structure:
These are the step to build a rock-paper-scissors game using python:

1. Import required libraries.
2. Initialize window.
3. Code for user choice.
4. Code for computer choice.
5. Define functions.
    5.1 Function to Start Game.
    5.2 Function to Reset.
    5.3 Function to Exit.
6. Define buttons.
7. Mainloop to run program.
"""

# 1. Import required libraries.
from tkinter import *
import random

# 2. Initialize window.
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Pizofreude - Rock, Paper, Scissors')
root.config(bg = 'seashell3')
# Label.
Label(root, text = 'Rock, Paper, Scissors', font='comicsans 20 bold', bg = 'seashell2').pack()

# 3. Code for user choice.
# Variable 1.
# user_take is a string type variable.
# Stores the choice that user enters.
user_take = StringVar()
Label(root, text = 'Choose one: rock, paper, scissors', font='comicsans 15 bold', bg = 'seashell2').place(x=20, y=70)
Entry(root, font = 'comicsans 15', textvariable = user_take, bg = 'antiquewhite2').place(x=90, y=130)

# 4. Code for computer choice.
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# 5. Define functions.
#     5.1 Function to Start Game.
# Variable 2.
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, you both select same!')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You loose, computer select paper!')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win, computer select scissors!')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You loose, computer select scissors!')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win, computer select rock!')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose, computer select rock!')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win, computer select paper!')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

#     5.2 Function to Reset.
def Reset():
    Result.set("") 
    user_take.set("")

#     5.3 Function to Exit.
def Exit():
    root.destroy()

# 6. Define buttons.
Entry(root, font = 'comicssans 10 bold', textvariable = Result, bg='antiquewhite2', width = 50,).place(x=25, y=250)

Button(root, font = 'comicsans 13 bold', text = 'PLAY', padx =5, bg='seashell4', command = play).place(x=150, y=190)

Button(root, font = 'comicsans 13 bold', text = 'RESET', padx =5, bg='seashell4', command = Reset).place(x=70, y=310)

Button(root, font = 'comicsans 13 bold', text = 'EXIT', padx =5, bg='seashell4', command = Exit).place(x=230, y=310)

# 7. Mainloop to run program.
root.mainloop()