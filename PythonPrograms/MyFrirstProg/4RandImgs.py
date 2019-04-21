from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import stat
from random import randint

if not(os.path.isfile('Paths.txt')):
	f= open("Paths.txt", "w+")
	f.close()


def AllPaths(Path_file, Path_ImgSet1, Path_imgSet2, Path_ImgSet3, Path_ImgSet4):
	f= open('Paths.txt', 'r')
	Path_file.append(f.readline())
	Path_ImgSet1.append(f.readline())
	Path_imgSet2.append(f.readline())
	Path_ImgSet3.append(f.readline())
	Path_ImgSet4.append(f.readline())
	f.close()


def file_len(fname):
	# Number of lines in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

f= open('Paths.txt', 'r')

f.readline()
ImgSet1_path = f.readline().strip('\n')
imgSet2_path = f.readline().strip('\n')
ImgSet3_path = f.readline().strip('\n')
ImgSet4_path = f.readline().strip('\n')
f.close()



# print(oct(stat.S_IMODE(os.lstat(imgSet2_path).st_mode)))


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
image_ImgSet1_name=(ImgSet1.readline())
'''




'''
imgSet2 = open("imgSet2.txt", "w+")
for i in (os.listdir(imgSet2_path)):
    imgSet2.write(i + '\n')
imgSet2.close()

imgSet2 = open("imgSet2.txt", 'r')

file_length = (file_len("imgSet2.txt"))
random_image_imgSet2 = randint(0, file_length - 1)

i = 0
while i < random_image_imgSet2:
    (imgSet2.readline())
    i = i + 1
image_imgSet2_name=(imgSet2.readline())
'''




'''
ImgSet3 = open("ImgSet3.txt", "w+")
for i in (os.listdir(ImgSet3_path)):
    ImgSet3.write(i + '\n')
ImgSet3.close()

ImgSet3 = open("ImgSet3.txt", 'r')

file_length = (file_len("ImgSet3.txt"))
random_image_ImgSet3 = randint(0, file_length - 1)

i = 0
while i < random_image_ImgSet1:
    (ImgSet3.readline())
    i = i + 1
image_ImgSet3_name=(ImgSet3.readline())
'''




'''
ImgSet4 = open("ImgSet4.txt", "w+")
for i in (os.listdir(ImgSet4_path)):
    ImgSet4.write(i + '\n')
ImgSet4.close()

ImgSet4 = open("ImgSet4.txt", 'r')

file_length = (file_len("ImgSet4.txt"))
random_image_ImgSet4 = randint(0, file_length - 1)

i = 0
while i < random_image_ImgSet4:
    (ImgSet4.readline())
    i = i + 1
image_ImgSet4_name=(ImgSet4.readline())




Global_Path = []
TempImgSet1_Link = []
TempLifeimgSet2entures_Link = []
TempImgSet3_Link = []
TempImgSet4_Link = []
AllPaths(Global_Path, TempImgSet1_Link, TempLifeimgSet2entures_Link, TempImgSet3_Link, TempImgSet4_Link)

The_ImgSet1ImageLink = (str(TempImgSet1_Link[0]).strip('\n') + '\\' + image_ImgSet1_name.strip('\n'))
The_LifeimgSet2entures_Link = (str(TempLifeimgSet2entures_Link[0]).strip('\n') + '\\' + image_imgSet2_name.strip('\n'))
The_ImgSet3_Link = (str(TempImgSet3_Link[0]).strip('\n') + '\\' + image_ImgSet3_name.strip('\n'))
The_ImgSet4_Link = (str(TempImgSet4_Link[0]).strip('\n') + '\\' + image_ImgSet4_name.strip('\n'))


# TK


root = Tk()
root.title("Random Mativational Image Displayer")
mainframe = ttk.Frame(root)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	



#The image widgets, their size... The size is static which need some work
#But they fit my screen okay for now.


ImgSet1_Img = ImageTk.PhotoImage(Image.open(The_ImgSet1ImageLink).resize((500, 375)))
myvar = Label(image=ImgSet1_Img)
myvar.image = ImgSet1_Img
myvar.grid(row=0, column=0)

LifeimgSet2entures_Img = ImageTk.PhotoImage(Image.open(The_LifeimgSet2entures_Link).resize((500, 375)))
myvar1 = Label(image=LifeimgSet2entures_Img)
myvar1.image = LifeimgSet2entures_Img
myvar1.grid(row=0, column=1)


ImgSet3_Img = ImageTk.PhotoImage(Image.open(The_ImgSet3_Link).resize((500, 375)))
myvar2 = Label(image=ImgSet3_Img)
myvar2.image = ImgSet3_Img
myvar2.grid(row=1, column=0)


ImgSet4_Img = ImageTk.PhotoImage(Image.open(The_ImgSet4_Link).resize((500, 375)))
myvar3 = Label(image=ImgSet4_Img)
myvar3.image = ImgSet4_Img
myvar3.grid(row=1, column=1)


def restart():
	os.system('Python 4RandImgs.py')
	sys.exit(0)

b = Button(root, text="Refresh", command=restart)
b.grid(row=0, column=2)

# Tk code end.

root.mainloop()
