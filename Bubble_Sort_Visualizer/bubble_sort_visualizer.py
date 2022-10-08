# Python Bubble Sort Visualizer
"""
Project Structure:
1. Importing necessary modules.
2. Initialising pygame and creating a window with declaration of necessary variables.
3. Defining functions to draw rectangles, show texts and implement bubble sort.
4. Taking user input and visualization of bubble sort.
5. Initialize game screen.
"""

# 1. Importing necessary modules.
"""
Pygame: open source library to create games and do other multimedia tasks.
It provides functions to create windows, shapes, read keyboard and mouse events.
"""
from turtle import bgcolor
import pygame

# 2. Initialising pygame and creating a window with declaration of necessary variables.
# Initialise pygame to create a window.
pygame.init()
# Title and icon.
pygame.display.set_caption("Bubble Sort Visualizer")
icon = pygame.image.load('bubble.ico')
pygame.display.set_icon(icon)
# array for user input variable, similar to StringVar in tkinter.
array1 = ""
array = []
# Define screen dimensions, declare font for viewing text.
screen = pygame.display.set_mode((700,500))
# None implies the default system font.
font = pygame.font.SysFont('roboto', 25)
# run: A variable to terminate the loop and close the window.
run = True

# 3. Defining functions to draw rectangles, show texts and implement bubble sort.
# Function to show text.
def show_text(array):  
   # Create a new screen.
   screen.fill('darkgrey')
   # Use the font to display the array.
   # RGB = Red, Green, Blue. Value = 0 - 255.
   block = font.render(str(array), True, (255,255,150))
   # Display the array.
   screen.blit(block, (20,20))

# Function to draw rectangles.
def draw_rect():
   for i in range(len(array)):
       # Draw rectangles using array elements.
       # To maintain gaps between rectangles, mention the top coordinate more than the width.
       pygame.draw.rect(screen, (255, 125, 0), ((50+i*25, 50, 20, array[i]*2)))
   pygame.display.update()

# Function to implement bubble sort Implementer using PyGame.
def bubble_sort():
   for i in range(len(array)):
       for j in range(len(array)-1):
           # Compare every element with every other element and switch places.
           # Similitude with a, b = b, a.
           if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
       # Display the array.
       array1 = [str(i) for i in array]
       array1 = ",".join(array1)
       show_text(array1)
       # Draw the rectangular boxes.
       draw_rect()
       # Keep a delay between changes in ms unit.
       pygame.time.delay(500)
       # Display the changes made.
       pygame.display.update()

# Initialize game screen.
# Initially fill the screen black.
screen.fill('grey')
block =  font.render("  Pizofreude's Guide for Visualization Of Bubble Sort", True, (0,0,0))  # RGB Color.
screen.blit(block, (0,20))
block1 =  font.render("  Enter Input and press ENTER to visualize", True, (255,255,150))
screen.blit(block1, (0,40))
block2 =  font.render("  Add comma to separate the integers and backspace to pop", True, (255,255,150))
screen.blit(block2, (0,60))
pygame.display.update()

# 4. Taking user input and visualization of bubble sort.
# Loop is applied to accomodate game updates.
while run == True: 
   # Detect keyboard press.
   for event in pygame.event.get():
       # Keyboard press condition.
       if event.type == pygame.KEYDOWN:
           # Spacebar press.
           if event.key == pygame.K_RETURN:
               # Start visualising and sorting.
               # Convert string to array by splitting the string.
               array = array1.split(",")
               array = [int(i) for i in array]
               draw_rect()
               pygame.time.delay(1500)
               bubble_sort()

           elif event.key == pygame.K_BACKSPACE:
               # Delete last element in the list using array1[:-1].
               array1 = array1[:-1]

           else:
                # Check if the keyboard press is a digit.
                    array1 += event.unicode
                    show_text(array1)
                    pygame.display.update()

       # Check if pygame exit is selected.
       elif event.type == pygame.QUIT:
        run = False
        
# Quit and close the window
pygame.quit()