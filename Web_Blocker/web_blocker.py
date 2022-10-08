# Python Website Blocker with GUI Tkinter library.
"""
Project Structure:
1. Importing the module.
2. Create the display window.
3. Create an entry widget.
4. Define web blocker function.
5. Create a block button.
6. Mainloop to run the program.
"""

# 1. Importing the module.
# GUI.
from tkinter import *
# Grant admin right for localhost/127.0.0.1.
import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Code of your program here

    # 2. Create the display window.
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Pizofreude - Website Blocker")
    root.iconbitmap('22website_102066.ico')
    # Label() widget is used to display one or more than one line of text
    # that users aren’t able to modify.
    Label(root, text ='WEBSITE BLOCKER' , font = 'roboto 20 bold').pack()
    Label(root, text ='Pizofreude', font = 'roboto 20 bold').pack(side=BOTTOM)

    # 3. Create an entry widget.
    # host_path stores the path of hosts file.
    host_path = 'C:\Windows\System32\drivers\etc\hosts'
    # ip_address stores the IP address used by localhost
    ip_address = '127.0.0.1'   # Alternative to localhost for web blocking.

    Label(root, text = 'Enter Website : ', font = 'roboto 13 bold').place(x=5 ,y=60)
    # wrap = WORD will break the line after the last word.
    # padx puts an extra bit space on left and right side of the widget.
    # pady puts extra space on top and bottom side of the widget.
    Websites = Text(root, font = 'arial 10', height='2', width='40', wrap = WORD, padx=5, pady=5)
    Websites.place(x=140, y=60)

    # 4. Define web blocker function.
    def Blocker():
        # website_lists get all the Websites to enter by the users.
        website_lists = Websites.get(1.0, END)
        # website_list(lists.split(“,”)) split the content of the lists by comma
        # and then convert it into list ad store it into Website.
        Website = list(website_lists.split(","))

        # with open: open the file and it will automatically close the 
        # file handler when we are done with it.
        # r+ will use to open a file for reading and writing.
        with open (host_path, 'r+') as host_file:
            file_content = host_file.read()
            for website in Website:
                if website in file_content:
                    Label(root, text = 'Already Blocked', font = 'roboto 12 bold').place(x=200, y=200)
                    pass
                else:
                    host_file.write(ip_address + " " + website + '\n')
                    Label(root, text = "Blocked", font = 'roboto 12 bold').place(x=230, y=200)

    # 5. Create a block button.
    # activebackground – sets the background color to use
    # when the button is click.
    block = Button(root, text = 'Block', font = 'roboto 12 bold', pady=5, command = Blocker, width=6, bg = 'grey', activebackground = 'darkgrey')

    block.place(x=230, y=150)

    # 6. Mainloop to run the program.
    root.mainloop()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)