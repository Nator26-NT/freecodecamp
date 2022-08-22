import tkinter as tk
from tkinter import filedialog , Text
import os

root = tk.Tk()

def addapp():
	filename = fikedialog.askopenfilename(initialdir="/" , tittle="select file"
	filetypes=(("executables" , "*.py" ) , ("all files " , "*/")))

canvas = tk.Canvas(root, height = 600 , width = 400 , bg= "black")
canvas.pack()
frame = tk.Frame(root , bg="white")
frame.place(relheight= 0.8 , relwidth= 0.8 , relx=0.1 , rely = 0.1)

open_file = tk.Button(root , text= "Open_file", padx=5 ,pady=10 , fg="white", bg="black")
open_file.pack()
run_Apps = tk.Button(root, text ="run_apps", fg="white", bg="black" , padx=5 ,pady= 10)
run_Apps.pack()








root.mainloop()
