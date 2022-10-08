# Voice Recorder Project in Python.
"""
Project File Structure:
Below is the flow of the python Voice recorder project.

1. Importing libraries.
2. Defining the functions for threading, recording voice and providing 
   a callback.
   2.1 threading_rec().
   2.2 callback().
   2.3 record_audio().
3. Creating the voice recorder GUI.
4. Create the components and the button.
5. Mainloop to run the program.
"""

# 1. Importing libraries.
# Sounddevice contains the functions to record voice input
# using the microphone.
import sounddevice as sd
# Import wildcard GUI library to create the GUI of the application.
from tkinter import *
# To use the data structure queue
import queue
# To save the audio recorded.
import soundfile as sf
# To simulate multithreading.
import threading
# Messagebox contains prompts to display to the user 
# when there is a missing input or when the file does not exist.
from tkinter import messagebox

# 2. Defining the functions for threading, recording voice and providing 
#    a callback.
#    2.1 threading_rec().
# Functions to play, stop and record audio in Python voice recorder.
# The recording is done as a thread to prevent it being the main process.
def threading_rec(x):
   if x == 1:
       # If recording is selected, then the thread is activated.
       t1 = threading.Thread(target = record_audio)
       t1.start()
   elif x == 2:
       #To stop, set the flag to false
       global recording
       recording = False
       messagebox.showinfo(message = "Recording finished")
   elif x == 3:
       #To play a recording, it must exist.
       if file_exists:
           #Read the recording if it exists and play it
           data, fs = sf.read("trial.wav", dtype='float32')
           sd.play(data, fs)
           sd.wait()
       else:
           #Display and error if none is found
           messagebox.showerror(message = "Record something to play")

#    2.2 callback().
# Fit data into queue.
def callback(indata, frames, time, status):
   # Queue is a data structure that follows FIFO.
   q.put(indata.copy())

#    2.3 record_audio().
# Recording function.
def record_audio():
   # Declare global variables.  
   global recording
   # Set to True to record.
   recording = True  
   global file_exists
   # Create a file to save the audio.
   messagebox.showinfo(message = "Recording Audio. Speak into the mic")
   with sf.SoundFile("trial.wav", mode='w', samplerate=44100,
                       channels=2) as file:
   # Create an input stream to record audio without a preset time.
           with sd.InputStream(samplerate=44100, channels=2, callback=callback):
               while recording == True:
                   # Set the variable to True to allow playing the audio later.
                   file_exists = True
                   # write into file.
                   file.write(q.get())

# 3. Creating the voice recorder GUI.
# Define the user interface for Voice Recorder using Python.
voice_rec = Tk()
voice_rec.geometry("360x200")
voice_rec.title("Pizofreude's Voice Recorder")
voice_rec.config(bg = "#c19510")
voice_rec.resizable(False, False)
# Create a queue to contain the audio data.
q = queue.Queue()
# Declare variables and initialise them.
recording = False
file_exists = False

# 4. Create the components and the button.
#Label to display app title in Python Voice Recorder Project
title_lbl  = Label(voice_rec, text="  Pizofreude Voice Recorder  ", font="14", bg="#f2cc5a").grid(row=0, column=0, columnspan=3)
 
#Button to record audio
record_btn = Button(voice_rec, text=" Record Audio ", font="12", command=lambda m=1:threading_rec(m))
#Stop button
stop_btn = Button(voice_rec, text="Stop Recording", font="6", command=lambda m=2:threading_rec(m))
#Play button
play_btn = Button(voice_rec, text="Play Recording", font="6", command=lambda m=3:threading_rec(m))
#Position buttons
record_btn.grid(row=1,column=1)
stop_btn.grid(row=1,column=0)
play_btn.grid(row=1,column=2)

# 5. Mainloop to run the program.
voice_rec.mainloop()
