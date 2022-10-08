# Countdown Timer in Python.
"""
Project Structure:
1. Importing modules: time, tkinter, and plyer.
2. Initializing the window and declaring the dimensions.
3. Defining functions for timer and placeholders.
4. Creating the user input interface.
5. Addition of a button to activate the timer.
6. Mainloop to run GUI program of Tkinter.
"""

# 1. Importing modules: time, tkinter, and plyer.
import time
# GUI.
# Alternative GUI libraries supported by python:
# PyQT5, Kivy, Pyside2.
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter.font import BOLD
# plyer to create desktop notifications.
"""
Plyer is a library that provides us with features to access bluetooth,
wifi, battery details, send emails, gps and so on.
Here we use notification to provide desktop notifications that get
displayed on completion of python countdown timer.
"""
from plyer import notification

# 2. Initializing the window and declaring the dimensions.
window = Tk()
window.geometry("600x200")
window.resizable(0,0)
window.title("Pizofreude - Countdown Timer & Notification")
window.iconbitmap('timer_icon_181212.ico')

# 3. Defining functions for timer and placeholders.
# Remove the placeholders for every entry field based on click.
def h_click(event):
    hour_entry.delete(0, 'end')        
def m_click(event):
    min_entry.delete(0, 'end')
def s_click(event):
    sec_entry.delete(0, 'end')

# Function to activate python countdown timer and show notifications
# once timer is up.
def timer():
   # Since we use placeholders, we check if the user entered an integer.
   try:
       timer_time = int(hour_entry.get())*3600 + int(min_entry.get())*60 + int(sec_entry.get())
      
   except:
       messagebox.showerror(message = "Enter Valid Time")
   # The user cannot activate a timer with no time set.
   # To update the timer with every decreasing second and display a notification.  
   if timer_time > 0:
       hour = 0
       min = 0
       sec = 0   
       # If minutes is more than 60, it has to be set to the next hour.
       while timer_time >= 0:
           min, sec = divmod(timer_time, 60)
           if min > 60:
               hour, min = divmod(min, 60)
           # Set the declared variables with the new values to display.              
           hours.set(hour)
           mins.set(min)
           secs.set(sec)
           # Sleep for 1 creates a delay of 1 second.
           time.sleep(1)  
           # Update the changes on the window for every second.
           window.update()
           # Decrement the timer value by 1.
           timer_time -= 1
       # Create a desktop notification.
       notification.notify(
       
        # notification.notify(): Creates a desktop notification.
        # It takes the parameters: title - title of the alert, message - message of the notification,
        # app_icon - (optional), a picture or icon, timeout - the duration after which the notification elapses.
        # Replace the path for app_icon with icon's absolute path.
    
           # Title of the notification.
           title = "TIMER ALERT",
           # Body of the notification.
           message = "Hej Kollege!\n Do what you wanted to achieve! \n Otherwise, try again with a new timer?!",
app_icon="./timer_icon_181212.ico",
           # Notification stays for 30 seconds.
           timeout  = 30,
       )
       # This notification is provided by tkinter with the created app.
       messagebox.showinfo(message="Your time is up!")

# 4. Creating the user input interface.
# Label for displaying the title of the app.
# Position of the label or widget is set using pack().
# pack() defaults to centered alignment on a x row and y column coordinate.
title_label_1 = Label(window, text=" Pizofreude - Countdown Timer & Notification", font=("Sans-Serif", 12, BOLD)).pack()
title_label_2 = Label(window, text=" Put 0 in the left out fields", font=("Sans-Serif", 11)).pack()
# Variables using which the timer is updated in the function.
hours = IntVar()
mins = IntVar()
secs = IntVar()
 
# To read user input for hours, minutes and seconds.
hour_entry = Entry(window, width=3, textvariable=hours, font=("Ubuntu Mono",18))
min_entry = Entry(window, width=3, textvariable=mins, font=("Ubuntu Mono",18))
sec_entry = Entry(window, width=3, textvariable=secs, font=("Ubuntu Mono",18))
 
# Placeholder for the entry widgets.
hour_entry.insert(0,00)
min_entry.insert(0,00)
sec_entry.insert(0,00)
 
# Positioning the entry widgets.
# place() takes an x(from the left) and y(from the top) coordinate.
hour_entry.place(x=80*2.14, y=40*1.5)
min_entry.place(x=130*2.14, y=40*1.5)
sec_entry.place(x=180*2.14, y=40*1.5)

# Entry widget labels. Remember: %H:%M:%S & %d:%m:%Y
hour_entry_label = Label(window, text="H   :", font=("Sans-Serif", 14, BOLD))
hour_entry_label.place(x=80*2.8, y=40*1.5)
min_entry_label = Label(window, text="M  :", font=("Sans-Serif", 14, BOLD))
min_entry_label.place(x=130*2.55, y=40*1.5)
sec_entry_label = Label(window, text="S", font=("Sans-Serif", 14, BOLD))
sec_entry_label.place(x=180*2.4, y=40*1.5)
 
# To link the defined placeholder removal functions on mouse click.
hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

# 5. Addition of a button to activate the timer.
# Button to activate the timer function.
button = Button(window, text=' Activate Timer ', font="UbuntuMono 12 bold", bg='Red', command=timer).pack(pady=40*1.5)
# Close the window and exit the app.

# 6. Mainloop to run GUI program of Tkinter.
window.mainloop()