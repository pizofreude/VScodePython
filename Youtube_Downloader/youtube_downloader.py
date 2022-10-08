# Python YouTube Downloader with Pytube.
"""
Project Structure:
1. Import Libraries.
2. Create Display Window.
3. Create Field to Enter Link.
4. Create Function to Start Downloading.
5. Mainloop to run program.
"""

# 1. Import Libraries.
# Tkinter standard GUI library for python.
from tkinter import *
# pytube used for downloading videos from youtube.
from pytube import YouTube

# 2. Create Display Window.
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Pizofreude - Youtube Video Downloader")
root.iconbitmap(default = 'youtube_social_circle_dark.ico')
Label(root,text = ' Youtube Video Downloader ', font = 'Roboto 20 bold').pack()

# 3. Create Field to Enter Link.
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Roboto 15 bold').place(x=160, y=60)
link_enter = Entry(root, width = 70, textvariable = link).place(x=32, y=90)

# 4. Create Function to Start Downloading.
def Downloader():
    """
    url variable gets the youtube link from the link variable by get() function
    and then str() will convert the link in string datatype.
    """
    def connection_status():
        try:
            yt = YouTube("https://www.youtube.com/")
            print("connection established")
        except:
            print("connection error")
    connection_status()
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'Roboto 15').place(x=180, y=210)  

Button(root, text = 'DOWNLOAD', font = 'Roboto 15 bold', bg = 'pale violet red', padx = 2, command = Downloader).place(x=180, y=150)

# 5. Mainloop to run program.
root.mainloop()