# Screen Recorder with Python.
"""
Project File Structure:
1. Importing libraries.
2. Creating the screen recording function.
3. Defining the GUI.
4. Create the components and the button.
5. Mainloop to run the program.
"""

# 1. Importing libraries.
# Take screenshot of the screen using ImageGrab.
from PIL import ImageGrab
# To write the captured screen to a video.
import cv2
# Convert images to arrays and vice versa.
import numpy as np
# Build the user interface of the application.
from tkinter import *

# 2. Creating the screen recording function.
def record_screen():
   # Get image dimensions.
   # Screen capture.
   """
   If you wish to record only a certain part of the screen or an app,
   use the parameter bbox().
   Parameters: left, top, right and bottom (clockwise from left to remember).
   """
   image = ImageGrab.grab()
   # Convert the object to numpy array.
   img_np_arr = np.array(image)
   # Extract and print shape of array.
   shape = img_np_arr.shape
   print(shape)
 
   # Create a video writer.
   screen_cap_writer = cv2.VideoWriter('screen_recorded.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 50, (shape[1], shape[0]))
 
   # To View the screen recording in a separate window (OPTIONAL).
   # This is optional. Use the aspect ratio scaling if you wish to view the screen recording simultaneously.
   # Low scale_by_percent implies smaller window.
   scale_by_percent = 50
   width = int(shape[1] * scale_by_percent / 100)
   height = int(shape[0] * scale_by_percent / 100)
   new_dim = (width, height)
 
   # Record the screen.
   # Condition to keep recording as a video.
   while True:
       # Capture screen.
       image = ImageGrab.grab()
       # Convert to array.
       img_np_arr = np.array(image)
       # OpenCV follows BGR and not RGB, hence we convert colour format.
       # Pillow uses RGB format whereas opencv uses BGR format.
       final_img = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR)
       # Write the frame to the video.
       screen_cap_writer.write(final_img)
       # OPTIONAL: To view screen recording in a separate window, resize and use imshow().

       '''
           If you choose to view the screen recording simultaneously,
           It will be displayed and also recorded in your video.
       '''
       image = cv2.resize(final_img, (new_dim))
       cv2.imshow("image", image)

       # Stop and exit screen recording if user presses 'q' (You can put any letter).
       if cv2.waitKey(1) == ord('q'):
           break
      
   # Release the created the objects.
   screen_cap_writer.release()
   cv2.destroyAllWindows()

# 3. Defining the GUI.
screen_recorder = Tk()
screen_recorder.iconbitmap(r"greenrecorder_94604.ico")
# Window is set to the dimensions of the bg_img.
screen_recorder.geometry("340x220")
screen_recorder.resizable(0,0)
screen_recorder.title("Pizofreuder Screen Recorder")
# Set a background image: Load the image using PhotoImage.
# This function is available in tkinter and it supports only PNG images.
bg_img = PhotoImage(file = "./BG_340x220.png")

# 4. Create the components and the button.
# bd=0:setting the border to 0 or no border.
label1 = Label(screen_recorder, image = bg_img, bd=0)
# Place the label in the first row, immediately after the top margin.
label1.pack()
# Create and place the components.
title_label = Label(screen_recorder, text=" Pizofreuder Screen Recorder ", font=("Ubuntu Mono", 16), bg="grey")
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)
info_label = Label(screen_recorder, text=" Hit 'q' to quit screen recording ", font=("UbuntuMono 10 bold"), bg="lightgrey")
# relx and rely: percentages of distance from the left and top respectively.
# Anchor=CENTER positions the element in the center.
info_label.place(relx=0.5, rely=0.3, anchor=CENTER)
screen_button = Button(screen_recorder, text="Record Screen", font=("UbuntuMono 10 bold"), command=record_screen, relief = RAISED)
screen_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# 5. Mainloop to run the program.
screen_recorder.mainloop()