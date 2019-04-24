from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import ctypes
import math
from datetime import date
from random import randint






def Exit():
	sys.exit(0)

# image transition
def fadeIn (img1, img2): #pass images here to fade between
        #while True:
        for IN in range(0,10):
                fadein = IN/10.0
                dst = cv2.addWeighted( img1, fadein, img2, fadein, 0)#linear $
                cv2.imshow('window', dst)
                cv2.waitKey(1)
                print(fadein)
                time.sleep(0.05)
                if fadein == 1.0: #blendmode mover
                        fadein = 1.0
        return # exit function



def file_len(fname):
	# Number of lines in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def insert_week():
	# Gets the text from the file and fills the Textfield1 with it
	global Weekfile
	Textfield1.delete('1.0', 'end')
	Weekfile = open('C:/Users/Entertainment/Desktop/FastGoals.txt')
	WeekContent = Weekfile.read()
	Weekfile.close()
	Textfield1.insert('1.0', WeekContent)



'''
Get's the file for the needed date.
'''
LogsListPath = 'C:/Users/Entertainment/Desktop/Portfolio/PythonPrograms/MorningRoutineApp/LogsArchiveTest/'
LogsList = open("LogsList.txt", "w+")
for i in (os.listdir(LogsListPath)):
    LogsList.write(i + '\n')
LogsList.close()


NumberOfLogs = (file_len("LogsList.txt"))
print(NumberOfLogs , ' -----------------')


DateIndexes = list(range(0, NumberOfLogs))
DateIndex = DateIndexes[NumberOfLogs - 1]
DictionaryOfLogs = []
LogsList = open("LogsList.txt", 'r')
for i in DateIndexes:
	DictionaryOfLogs.append(LogsList.readline().strip('\n').strip('~$'))
	i = i + 1
DictionaryOfLogs.sort()
DictionaryOfLogs.pop(0)


CurrentIndex = NumberOfLogs - 2
print(CurrentIndex, ' is the current index')
"""
The next two functions are for the buttons '<' and '>' and serve to display the 
needed file content in textfield1
"""
def ForwardCurrentIndex():
	global CurrentIndex
	if CurrentIndex < (NumberOfLogs - 2):
		CurrentIndex = CurrentIndex + 1
		Textfield2.delete('1.0', 'end')
		CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex])
		CurrentLogContent = CurrentLogFile.read()
		CurrentLogFile.close()
		Textfield2.insert('1.0', CurrentLogContent)
		print(CurrentIndex, 'is the CurrentIndex')


def BackwardCurrentIndex():
	global CurrentIndex
	if CurrentIndex > 0:
		CurrentIndex = CurrentIndex - 1
		print(CurrentIndex, ' is the CurrentIndex index')
		Textfield2.delete('1.0', 'end')
		CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex])
		CurrentLogContent = CurrentLogFile.read()
		CurrentLogFile.close()
		Textfield2.insert('1.0', CurrentLogContent)


def SaveChanges():
	SavingFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex], 'w')
	SavingFile.write(Textfield2.get('1.0', 'end'))
	SavingFile.close()
	'''
	# Doesn't work yet
	SavingFile = open(Weekfile, 'w')
	SavingFile.write(Textfield1.get('1.0', 'end'))
	SavingFile.close()
	'''



print(LogsListPath + DictionaryOfLogs[CurrentIndex])



ImgSet1_path = "C:/HardDriveTempoCopy/MULTIBOOT/Pictures/DreamBoard/Gals/Women/"
imgSet2_path = "C:/HardDriveTempoCopy/MULTIBOOT/Pictures/DreamBoard/Gals/Women/"



# ----get the needed random image path:----
ImgSet1 = open("ImgSet1.txt", "w+")
for i in (os.listdir(ImgSet1_path)):
    ImgSet1.write(i + '\n')
ImgSet1.close()

ImgSet1 = open("ImgSet1.txt", 'r')

file_length = (file_len("ImgSet1.txt"))
random_image_ImgSet1 = randint(0, file_length - 1)

i = 0
while i < random_image_ImgSet1:
    (ImgSet1.readline())
    i = i + 1
image_ImgSet1_name=(ImgSet1_path + ImgSet1.readline().strip('\n'))
print(image_ImgSet1_name)










user32 = ctypes.windll.user32
collumnwidth, rowheight =  math.trunc(user32.GetSystemMetrics(0) / 24) , math.trunc(user32.GetSystemMetrics(1) / 28)
CollumnWidth, RowHeight = 5 * collumnwidth, 14 * rowheight
print(CollumnWidth, RowHeight)

'''
Tk Code:

'''
# Create & Configure root
root = Tk()
root.title("Random Mativational Image Displayer")
root.attributes("-fullscreen", True)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)


# Create & Configure frame
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)




# Create a 5x10 (rows x columns) grid inside the frame
for x in range(23):
  Grid.columnconfigure(frame, x, weight=1)

Range = {1, 2}
for y in Range:
  Grid.rowconfigure(frame, y, weight=1)


# Getting the needed image sizes

im1 = Image.open("C:/HardDriveTempoCopy/MULTIBOOT/Pictures/DreamBoard/Gals/Women/17267385_726769827510669_6374602035660062720_n.jpg")
img1_width, img1_height = im1.size
a = img1_width / 300
b = img1_height / RowHeight

print(a, b)
if a >= b:
	c = a
else:
	c = b


print(c)

img1_width, img1_height = round(img1_width / c) , round(img1_height / c)

img1 = ImageTk.PhotoImage(im1.resize((img1_width, img1_height)), Image.ANTIALIAS)
Img1 = Label(frame, image=img1)
Img1.grid(row=1, column=18, columnspan=6)


im2 = Image.open(image_ImgSet1_name)
img2_width, img2_height = im2.size
a = img2_width / 300
b = img2_height / RowHeight

print(a, b)
if a >= b:
	c = a
else:
	c = b


print(type(c))

img2_width, img2_height = math.ceil(img2_width / c) , math.ceil(img2_height / c)

img2 = ImageTk.PhotoImage(im2.resize((img2_width, img2_height)), Image.ANTIALIAS) # Image.[Somehing] check it, might find the silution to the resizing problem
Img2 = Label(frame, image=img2)
Img2.img2 = img2
Img2.grid(row=2, column=18, columnspan=6) #, column=19, rowspan=12, columnspan=5)






button1 = Button(frame, text='week', width= 2 * collumnwidth, command=insert_week)
button1.grid(row=0, column=0, columnspan=2, sticky='NSEW')
button2 = Button(frame, text='month', width= 2 * collumnwidth)#, command=)
button2.grid(row=0, column=2, columnspan=2, sticky='NSEW')
button3 = Button(frame, text='semester', width= 2 * collumnwidth)#, command=)
button3.grid(row=0, column=4, columnspan=2, sticky='NSEW')
button4 = Button(frame, text='<', width= collumnwidth, command=BackwardCurrentIndex)
button4.grid(row=0, column=6)
Label1 = Label(frame, text=date.today(), width= 10* collumnwidth)#, command=)
Label1.grid(row=0, column=7, columnspan=10, sticky='NSEW')
button6 = Button(frame, text='>', width= collumnwidth, command=ForwardCurrentIndex)
button6.grid(row=0, column=17)
button7 = Button(frame, text='Logs', width= 2 * collumnwidth)#, command=)
button7.grid(row=0, column=18, columnspan=2, sticky='NSEW')
button8 = Button(frame, text='Save Changes', width= 3 * collumnwidth, command=SaveChanges)
button8.grid(row=0, column=20, columnspan=3, sticky='NSEW')





def exit():
	sys.exit(0)

button9 = Button(frame, text="X", command=exit)
button9.grid(row=0, column=23,  sticky='NSEW')





Textfield1 = Text(frame,  bg="lightgrey")
Textfield1.grid(row=1, column=0, columnspan=6, rowspan=2, sticky='NSEW')


Textfield2 = Text(frame,  bg="white")
Textfield2.grid(row=1, column=6, columnspan=12, rowspan=2, sticky='NSEW')

CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex], 'r')
CurrentLogContent = CurrentLogFile.read()
CurrentLogFile.close()
Textfield2.insert('1.0', CurrentLogContent)



root.mainloop()