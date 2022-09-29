import _tkinter
from email.mime import image
from logging import root
from re import T
import tkinter
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('600x600')
root.title('Dice Roll Simulation')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="\n\n")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text=" Hello from Hafeez ",
                fg="blue",
                bg="gold",
                font="comicsans 16 bold")
HeadingLabel.pack()

# images
dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png',]
# simulating the dice with random numbers between
# 0 to 6 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget 
ImageLabel.pack(expand=True) #expand=True auto centralize the image in the root window

# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text="Roll the Dice", fg='black', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)



# call the mainloop of Tk
# keeps window open
root.mainloop()
