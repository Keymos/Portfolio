from tkinter import *
from tkinter import ttk
import os



def Exit():
	sys.exit(0)

'''

Tk Code:

'''
root = Tk()
root.title("Random Mativational Image Displayer")
root.attributes("-fullscreen", True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	

Exit_button = Button(root, text="X", command=Exit )
Exit_button.grid(column=0, row=1)

test1= ttk.Label(text="Test1")
test1.grid(column=0, row=0)











root.mainloop()