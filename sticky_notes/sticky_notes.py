# Python Sticky Notes project.
# Practice database with UI.
# Python built-in database: SQLite3 package.
    # SQLite3 package stores and access the notes.
"""
Project File Structure:
Below is the flow of the sticky notes python project.

1. Importing necessary libraries.
2. Creating a connection with the database and creating a table.
3. Declaring functions to take, edit, view and delete notes.
4. Creating a user interface.
"""

# 1. Importing necessary libraries/modules.
import sqlite3 as sql
from tkinter import *  # Wildcard to import modules as necessaries.
from tkinter import messagebox
from turtle import title

# 2. Creating a connection with the database and creating a table.
try:
    con = sql.connect('sticky_notes.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE notes_table
                        (date text, notes_title text, notes text)''')
except:
    print('Connected to table of database')

# 3. Declaring functions to take, edit, view and delete notes.
def add_notes():
    # Get input values.
    today = date_entry.get()
    notes_title = notes_title_entry.get()
    notes = notes_entry.get("1.0", "end-1c")    # Specify the index for a text widget (1.0 to end-1c).
    # Raise a prompt of missing values.
    if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 0):
        messagebox.showerror(message = "ENTER REQUIRED DETAILS.")
    else:
        # Insert into the table.
        # Formatting operator %s to replace inputs in the required fields.
        cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
        messagebox.showinfo(message="Noted added")
        # Commit to preserve changes.
        con.commit()

# Display all the notes.
def view_notes():
        # Get all the user input.
        date = date_entry.get()
        notes_title = notes_title_entry.get()
        # If no input is given, get all notes.
        if (len(date) <= 0) & (len(notes_title) <= 0):
                sql_statement = "SELECT * FROM notes_table"
                
        # Get notes matching a title.
        elif (len(date) <= 0) & (len(notes_title) > 0):
                sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title
        # Get notes matching a date.
        elif (len(date) > 0) & (len(notes_title) <= 0):
                sql_statement = "SELECT * FROM notes_table where date ='%s'" %date
        # Get notes matching the date and title.
        else:
                sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
                
        # Execute the query.
        cur.execute(sql_statement)
        # Get all the contents of the query.
        row = cur.fetchall()
        # Check if none was obtained.
        if len(row) <= 0:
                messagebox.showerror(message="No note found")
        else:
                #Print the notes
                for i in row:
                        messagebox.showinfo(message="Date: "+i[0]+"\nTitle: "+i[1]+"\nNotes: "+i[2])

# Delete notes.
def delete_notes():
    # Get input values.
    date = date_entry.get()
    notes_title = notes_title_entry.get()
    # User confirmation to delete.
    choice = messagebox.askquestion(message="Delete ALL notes?")
    # If yes selected, delete all.
    if choice == 'yes':
        sql_statement = "DELETE FROM notes_table"
    else:
        # Delete notes matching the date and title given.
        if (len(date) <= 0) & (len(notes_title) <= 0):
            # Raise error for zero input.
            messagebox.showerror(message="ENTER REQUIRED DETAILS")
            return
        else:
            sql_statement = "DELETE FROM notes_table where date = '%s' and notes_title = '%s'" %(date, notes_title)
    # Execute the query.
    cur.execute(sql_statement)
    messagebox.showinfo(message="Note(s) Deleted")
    con.commit()

# Update notes.
def update_notes():
    # Get user input.
    today = date_entry.get()
    notes_title = notes_title_entry.get()
    notes = notes_entry.get("1.0", "end-1c")
    # Check if input is given by the user.
    if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <=0):
        messagebox.showerror(message = "ENTER REQUIRED DETAILS")
    # Update notes.
    else:
        sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" %(notes, today, notes_title)
    # Execute query.
    cur.execute(sql_statement)
    messagebox.showinfo(message="Note Updated")
    con.commit()

# 4. Creating a user interface.
# Invoke call to class for a window.
window = Tk()
# Set dimensions of window and title.
window.geometry("500x300")
window.title("Sticky Note - Pizofreude")

title_label = Label(window, text="Stick you note!").pack()
# Read input.
## date_entry.
date_label = Label(window, text="Date:").place(x=10,y=20)
date_entry = Entry(window,  width=20)
date_entry.place(x=50,y=20)
## notes_title_entry.
notes_title_label = Label(window, text="Notes title:").place(x=10,y=50)
notes_title_entry = Entry(window,  width=30)
notes_title_entry.place(x=80,y=50)
## notes_entry.
notes_label = Label(window, text="Notes:").place(x=10,y=90)
notes_entry = Text(window, width=50,height=5)
notes_entry.place(x=60,y=90)

# Sticky notes buttons.
button1 = Button(window,text='Add Notes', bg = 'lightgrey', fg='black', command=add_notes).place(x=10,y=190)
button2 = Button(window,text='View Notes', bg = 'lightgrey', fg='black', command=view_notes).place(x=110,y=190)
button3 = Button(window,text='Delete Notes', bg = 'lightgrey', fg='black', command=delete_notes).place(x=210,y=190)
button4 = Button(window,text='Update Notes', bg = 'lightgrey', fg='black', command=update_notes).place(x=320,y=190)

# Mainloop and close app.
window.mainloop()
con.close()  # Close the connection with the database.














