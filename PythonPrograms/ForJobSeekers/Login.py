from tkinter import *
from tkinter import ttk
import subprocess
import os


def file_len(fname):
	# Number of lines in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def Login():
	# If Username and password both are 'admin' > opens adminPanel.py
	# Otherwise checks if the user is in the database, if so, remembers the current
	# user in CurrentUSerFile.txt and opens UserPanel.py
	CurrentUserFileIndex = []
	CurrentUser = [TextField_Username.get("1.0", END).strip('\n'), TextField_Password.get("1.0", END).strip('\n')]
	UsersDatabase = open('UsersDatabase.txt','r')
	if TextField_Username.get("1.0", END).strip('\n') == 'admin':
		if TextField_Password.get("1.0", END).strip('\n') == 'admin':
			subprocess.run(["Python", "AdminPanel.py"])
		else:
			print('Error')
	elif CurrentUser in UserDataBaseList:
		for i in os.listdir('List of JobSeekers'):
			Tempor = open('List of JobSeekers/%s' % i, 'r')
			j = 0
			while j < 9:
				Tempor.readline()
				j += 1
			if Tempor.readline() == ('>>> ' + CurrentUser[0] + ';;; ' + CurrentUser[1] ):
				CurrentUserFileIndex.append(int(i.strip('.txt')))
				print(CurrentUserFileIndex[0])
		UsersDatabase.close()
		CurrentUserFile = open('CurrentUserFile.txt', 'w+')
		jjj =  str(CurrentUserFileIndex[0])
		CurrentUserFile.write(str(CurrentUser) + jjj)
		CurrentUserFile.close()
		subprocess.run(["Python", "UserPanel.py"])
	else:
		print('Error')


def Register():
	# Checks if Username and Password combination is unique in the
	# UserDatabase.txt file, if so, adds it to the database. 
	CurrentUser = [TextField_Username.get("1.0", END).strip('\n'), TextField_Password.get("1.0", END).strip('\n')]
	if CurrentUser in UserDataBaseList:
		print('Error')
	elif ';;;' in TextField_Username.get("1.0", END).strip('\n') or ';;;' in TextField_Password.get("1.0", END).strip('\n'):
		print('Error')
	else: 
		UserDataBaseList.append(CurrentUser)
		TotalUsers =+ 1
		UsersDatabase = open('UsersDatabase.txt','a+')
		y = str('\n' + TextField_Username.get("1.0", END).strip('\n') + ';;; ' + TextField_Password.get("1.0", END).strip('\n'))
		UsersDatabase.write(y)
		UsersDatabase.close()
		temp = (os.listdir("List of JobSeekers"))
		tempo = int(str(temp[len(temp)-1]).strip(".txt"))+1
		UsersDatabase = open('List of JobSeekers/%s.txt' % str(tempo).zfill(8),'w+')
		i = 0
		UsersDatabase.write(9*'\n')
		UsersDatabase.write('>>> ' + CurrentUser[0] + ';;; ' + CurrentUser[1] )

# Users' Informations retreival if the database is there, otherwise
# create a new one.
if os.path.isfile('UsersDatabase.txt') == False:
	UsersDatabase = open('UsersDatabase.txt', 'w+')
	UsersDatabase.close()
TotalUsers = file_len('UsersDatabase.txt')
UsersDatabase = open('UsersDatabase.txt', 'r+')
UserDataBaseList = []
i = 0
while i < TotalUsers:
	x =  str(UsersDatabase.readline()).strip('\n').split(';;; ')
	UserDataBaseList.append(x)
	i += 1

# Checks if Jobs' Database file is present, if not, creates one.
if os.path.isfile('JobsDatabase.txt') == False:
	JobsDatabase = open('JobsDatabase.txt', 'w+')
	JobsDatabase.close()


# GUI:
root = Tk()
root.title("Hire now")

frame = Frame(root, height=100)
frame.grid(row=0, column=0, sticky=N + S + E + W)

Label_Username = Label(frame, text="Username:", padx=10, pady=7)
Label_Username.grid(row=0, column=0)

TextField_Username = Text(frame, height=1, width=20)
TextField_Username.grid(row=0, column=1)

Label_Password = Label(frame, text="Password:", padx=10, pady=7)
Label_Password.grid(row=1, column=0)

TextField_Password = Text(frame, height=1, width=20)
TextField_Password.grid(row=1, column=1)

Button_Login = Button(frame, text='Log In', padx=5, command=Login)
Button_Login.grid(row=0, column=2, columnspan=2)

Button_Register = Button(frame, text='Register', command=Register)
Button_Register.grid(row=1, column=2, columnspan=2)

root.mainloop()
