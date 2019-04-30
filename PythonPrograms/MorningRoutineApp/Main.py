from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import ctypes
import math
from datetime import datetime, date
from random import randint
from threading import Timer, Thread
import time


def PrintIt():
	print('hey')

def TheTimer():
	o = 0
	while o < 10:
		Change_Images()
		time.sleep(6.0)
		o += 1
		if o == 9:
			o = 0



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




weekFilePath = 'C:/Users/Entertainment/Desktop/WeekGoals.txt'
def insert_week():
	global First_Textfield_index
	# Gets the text from the file and fills the Textfield1 with it
	global Weekfile
	Textfield1.delete('1.0', 'end')
	Weekfile = open(weekFilePath)
	WeekContent = Weekfile.read()
	Weekfile.close()
	Textfield1.insert('1.0', WeekContent)
	First_Textfield_index = 1


monthFilePath = 'C:/Users/Entertainment/Desktop/1MonthGoals.txt'
def insert_month():
	global First_Textfield_index
	# Gets the text from the file and fills the Textfield1 with it
	global monthfile
	Textfield1.delete('1.0', 'end')
	monthfile = open(monthFilePath)
	monthContent = monthfile.read()
	monthfile.close()
	Textfield1.insert('1.0', monthContent)
	First_Textfield_index = 2

SixmonthFilePath = 'C:/Users/Entertainment/Desktop/6MonthGoals.txt'
def insert_6month():
	global First_Textfield_index
	# Gets the text from the file and fills the Textfield1 with it
	global Sixmonthfile
	Textfield1.delete('1.0', 'end')
	Sixmonthfile = open(SixmonthFilePath)
	SixmonthContent = Sixmonthfile.read()
	Sixmonthfile.close()
	Textfield1.insert('1.0', SixmonthContent)
	First_Textfield_index = 3


'''
Get's the file for the needed date.
'''
LogsListPath = 'C:/Users/Entertainment/Desktop/Portfolio/PythonPrograms/MorningRoutineApp/LogsArchiveTest/'
LogsList = open("LogsList.txt", "w+")
for i in (os.listdir(LogsListPath)):
    LogsList.write(i + '\n')
LogsList.close()


NumberOfLogs = (file_len("LogsList.txt"))


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



def BackwardCurrentIndex():
	global CurrentIndex
	if CurrentIndex > 0:
		CurrentIndex = CurrentIndex - 1
		Textfield2.delete('1.0', 'end')
		CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex])
		CurrentLogContent = CurrentLogFile.read()
		CurrentLogFile.close()
		Textfield2.insert('1.0', CurrentLogContent)


def SaveChanges():
	SavingFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex], 'w')
	SavingFile.write(Textfield2.get('1.0', 'end'))
	SavingFile.close()
	# Doesn't work yet
	global First_Textfield_index
	if First_Textfield_index == 1:
		SavingFile = open(weekFilePath, 'w')
	elif First_Textfield_index == 2:
		SavingFile = open(monthFilePath, 'w')
	elif First_Textfield_index == 3:
		SavingFile = open(SixmonthFilePath, 'w')
	
	SavingFile.write(Textfield1.get('1.0', 'end'))
	SavingFile.close()



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
global image_ImgSet1_name
i = 0
while i < random_image_ImgSet1:
    (ImgSet1.readline())
    i = i + 1
image_ImgSet1_name=(ImgSet1_path + ImgSet1.readline().strip('\n'))
ImgSet1.close()

global image_ImgSet2_name
ImgSet1 = open("ImgSet1.txt", 'r')
random_image_ImgSet2 = randint(0, file_length - 1)

i = 0
while i < random_image_ImgSet2:
    (ImgSet1.readline())
    i = i + 1
image_ImgSet2_name = (ImgSet1_path + ImgSet1.readline().strip('\n'))

def Change_Images():
	# ----get the needed random image path:----
	ImgSet1 = open("ImgSet1.txt", "w+")
	for i in (os.listdir(ImgSet1_path)):
	    ImgSet1.write(i + '\n')
	ImgSet1.close()

	ImgSet1 = open("ImgSet1.txt", 'r')

	file_length = (file_len("ImgSet1.txt"))
	random_image_ImgSet1 = randint(0, file_length - 1)

	global image_ImgSet1_name
	i = 0
	while i < random_image_ImgSet1:
	    (ImgSet1.readline())
	    i = i + 1
	image_ImgSet1_name=(ImgSet1_path + ImgSet1.readline().strip('\n'))
	ImgSet1.close()
	
	global image_ImgSet2_name

	ImgSet1 = open("ImgSet1.txt", 'r')
	random_image_ImgSet2 = randint(0, file_length - 1)
	
	i = 0
	while i < random_image_ImgSet2:
	    (ImgSet1.readline())
	    i = i + 1
	image_ImgSet2_name = (ImgSet1_path + ImgSet1.readline().strip('\n'))

	im1 = Image.open(image_ImgSet1_name)
	img1_width, img1_height = im1.size
	a = img1_width / 300
	b = img1_height / RowHeight

	if a >= b:
		c = a
	else:
		c = b

	img1_width, img1_height = round(img1_width / c) , round(img1_height / c)
	img1 = ImageTk.PhotoImage(im1.resize((img1_width, img1_height)), Image.ANTIALIAS)
		
	im2 = Image.open(image_ImgSet2_name)
	img2_width, img2_height = im2.size
	a = img2_width / 300
	b = img2_height / RowHeight


	if a >= b:
		c = a
	else:
		c = b







	img2_width, img2_height = math.ceil(img2_width / c) , math.ceil(img2_height / c)

	img2 = ImageTk.PhotoImage(im2.resize((img2_width, img2_height)), Image.ANTIALIAS) # Image.[Somehing] check it, might find the silution to the resizing problem
	Img2.configure(image=img2)
	Img2.img2 = img2

	Img1.configure(image=img1)
	Img1.img1 = img1


user32 = ctypes.windll.user32
collumnwidth, rowheight =  math.trunc(user32.GetSystemMetrics(0) / 24) , math.trunc(user32.GetSystemMetrics(1) / 28)
CollumnWidth, RowHeight = 5 * collumnwidth, 14 * rowheight


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

im1 = Image.open(image_ImgSet1_name)
img1_width, img1_height = im1.size
a = img1_width / 300
b = img1_height / RowHeight


if a >= b:
	c = a
else:
	c = b


img1_width, img1_height = round(img1_width / c) , round(img1_height / c)

img1 = ImageTk.PhotoImage(im1.resize((img1_width, img1_height)), Image.ANTIALIAS)
Img1 = Label(frame, image=img1)
Img1.grid(row=1, column=18, columnspan=6)


im2 = Image.open(image_ImgSet2_name)
img2_width, img2_height = im2.size
a = img2_width / 300
b = img2_height / RowHeight


if a >= b:
	c = a
else:
	c = b


img2_width, img2_height = math.ceil(img2_width / c) , math.ceil(img2_height / c)

img2 = ImageTk.PhotoImage(im2.resize((img2_width, img2_height)), Image.ANTIALIAS) # Image.[Somehing] check it, might find the silution to the resizing problem
Img2 = Label(frame, image=img2)
Img2.img2 = img2
Img2.grid(row=2, column=18, columnspan=6)






button1 = Button(frame, text='week', width= 2 * collumnwidth, command=insert_week)
button1.grid(row=0, column=0, columnspan=2, sticky='NSEW')
button2 = Button(frame, text='month', width= 2 * collumnwidth, command=insert_month)
button2.grid(row=0, column=2, columnspan=2, sticky='NSEW')
button3 = Button(frame, text='semester', width= 2 * collumnwidth, command=insert_6month)
button3.grid(row=0, column=4, columnspan=2, sticky='NSEW')
button4 = Button(frame, text='<', width= collumnwidth, command=BackwardCurrentIndex)
button4.grid(row=0, column=6)
Label1 = Label(frame, text=date.today(), width= 10* collumnwidth)
Label1.grid(row=0, column=7, columnspan=10, sticky='NSEW')
button6 = Button(frame, text='>', width= collumnwidth, command=ForwardCurrentIndex)
button6.grid(row=0, column=17)
button7 = Button(frame, text='SaveChanges', width= 2 * collumnwidth, command=SaveChanges)#, command=)
button7.grid(row=0, column=18, columnspan=2, sticky='NSEW')
button8 = Button(frame, text='Change Images', width= 3 * collumnwidth, command=Change_Images)
button8.grid(row=0, column=20, columnspan=3, sticky='NSEW')





def exit():
	sys.exit(0)

button9 = Button(frame, text="X", command=exit)
button9.grid(row=0, column=23,  sticky='NSEW')





Textfield1 = Text(frame,  bg="lightgrey", wrap=WORD)
Textfield1.grid(row=1, column=0, columnspan=6, rowspan=2, sticky='NSEW')


Textfield2 = Text(frame,  bg="white", wrap=WORD)
Textfield2.grid(row=1, column=6, columnspan=12, rowspan=2, sticky='NSEW')

CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex], 'r')
CurrentLogContent = CurrentLogFile.read()
CurrentLogFile.close()


DateAndTimeIndex = CurrentLogContent.find('/20')-5 
DateOfToday = datetime.today().strftime('%d/%m/%Y')
if (CurrentLogContent[DateAndTimeIndex:DateAndTimeIndex+10]) != DateOfToday:
	CurrentIndex += 1
	Logs_List = open("LogsList.txt", 'r')

	fileLength = (file_len("LogsList.txt") - 2)
	z = 0
	while z < fileLength:
		Logs_List.readline()
		z += 1
	NewDayLogFileName = (int(Logs_List.readline()[3:6])+1)
	#if NewDayLogFileName 
	if (NewDayLogFileName // 100) != 0:
		NewDayLogFileName = str(NewDayLogFileName)
	elif (NewDayLogFileName // 10) != 0:
		NewDayLogFileName = '0' + str(NewDayLogFileName)
	else:
		NewDayLogFileName = '00' + str(NewDayLogFileName)
	NewDayLogFileName = 'Day' + str(NewDayLogFileName + '.txt')
	DictionaryOfLogs.append(NewDayLogFileName)

	CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex], 'w+')
	CurrentLogFile.write('	'+ DateOfToday)
	CurrentLogContent = CurrentLogFile.read()
	CurrentLogFile.close()

CurrentLogFile = open(LogsListPath + DictionaryOfLogs[CurrentIndex], 'r')
CurrentLogContent = CurrentLogFile.read()
CurrentLogFile.close()
Textfield2.insert('1.0', CurrentLogContent)

LogsListPath = 'C:/Users/Entertainment/Desktop/Portfolio/PythonPrograms/MorningRoutineApp/LogsArchiveTest/'
LogsList = open("LogsList.txt", "w+")
for i in (os.listdir(LogsListPath)):
    LogsList.write(i + '\n')
LogsList.close()


NumberOfLogs = (file_len("LogsList.txt"))


# Images change every 6 seconds
threadedTimer = Thread(target=TheTimer, daemon=True)
threadedTimer.start()


root.mainloop()


# remember to make the app add a log if today's log doesn't have a file.