# Convert Text to Speech in Python.
"""
Project structure:
1. Importing the modules/libraries.
2. Create the display window.
3. Function to Convert Text to Speech in Python.
4. Function to Exit.
5. Function to Reset.
6. Define Buttons.
7. mainloop to run the program.
"""

# 1. Importing the modules/libraries.
from tkinter import *
# gTTS (Google Text-to-Speech) is a Python library, which is a very easy library that converts the text into audio.
from gtts import gTTS
# The playsound module is used to play audio files. With this module, we can play a sound file with a single line of code.
from playsound import playsound

# 2. Create the display window.
root = Tk()
root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("Pizofreude - TEXT TO SPEECH")

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Pizofreude", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()  # StringVar is a string type variable.
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
# textvariable used to retrieve the current text to entry widget.
entry_field = Entry(root, textvariable = Msg ,width ='50')  # Entry is used to create an input text field.
entry_field.place(x=20,y=100)

# 3. Function to Convert Text to Speech in Python.
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Pizofreude.mp3')
    playsound('Pizofreude.mp3')

# 4. Function to Exit.
def Exit():
    root.destroy()

# 5. Function to Reset.
def Reset():
    Msg.set("")

# 6. Define Buttons.
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

# 7. mainloop is a method to run the program.
root.mainloop()