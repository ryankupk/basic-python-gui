import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
#list to hold apps that have been selected
apps = []

#if the save.txt file already exists, read from it and populate apps list
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        #read contents of save.txt file
        tempApps=f.read()
        #split on comma into array
        tempApps = tempApps.split(',')
        #assign strings to apps array from file text, stripping to remove empty entries
        apps = [x for x in tempApps if x.strip()]

#function to add app to apps list
def addApp():
    #remove any entries currently in frame
    for widget in frame.winfo_children():
        widget.destroy()

    #assign fileName variable to string given from file explorer
    fileName = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    
    #when fileName is retrieved, append to apps list
    if fileName not in apps: apps.append(fileName)
    #create a label for each app in the frame
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

#function to run selected apps
def runApps():
    for app in apps:
        os.startfile(app)

#create canvas
canvas = tk.Canvas(root, height=700, width=700, bg="#263d42")
canvas.pack()

#create frame to which the apps will be listed
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely = 0.1)

#button to open files
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263d42", command=addApp)
openFile.pack()

#button to run selected files
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263d42", command=runApps)
runApps.pack()

root.mainloop()

#on startup, add labels to frame based on selected apps
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

#on close, save already selected apps to save.txt for use in the future
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')