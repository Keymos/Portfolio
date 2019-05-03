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
	CurrentUser = [TextField_Username.get("1.0", END).strip('\n'), TextField_Password.get("1.0", END).strip('\n')]
	UsersDatabase = open('UsersDatabase.txt','r')
	if TextField_Username.get("1.0", END).strip('\n') == 'admin':
		if TextField_Password.get("1.0", END).strip('\n') == 'admin':
			subprocess.run(["Python", "AdminPanel.py"])
		else:
			print('Error')
	elif CurrentUser in UserDataBaseList:
		UsersDatabase.close()
		CurrentUserFile = open('CurrentUserFile.txt', 'w+')
		CurrentUserFile.write(str(CurrentUser))
		CurrentUserFile.close()
		subprocess.run(["Python", "UserPanel.py"])


def Register():
	CurrentUser = [TextField_Username.get("1.0", END).strip('\n'), TextField_Password.get("1.0", END).strip('\n')]
	if CurrentUser in UserDataBaseList:
		print('Error')
	else:
		UserDataBaseList.append(CurrentUser)
		TotalUsers =+ 1
		UsersDatabase = open('UsersDatabase.txt','a+')
		y = str('\n' + TextField_Username.get("1.0", END).strip('\n') + '; ' + TextField_Password.get("1.0", END).strip('\n'))
		UsersDatabase.write(y)
		UserDataBase.close()

# Users' Informations retreival:

if os.path.isfile('UsersDatabase.txt') == False:
	UsersDatabase = open('UsersDatabase.txt','w+')
	UsersDatabase.close()

TotalUsers = file_len('UsersDatabase.txt')
print(TotalUsers)

UsersDatabase = open('UsersDatabase.txt','r+')
UserDataBaseList = []
i = 0
while i < TotalUsers:
	x =  str(UsersDatabase.readline()).strip('\n').split('; ')
	UserDataBaseList.append(x)
	i += 1
print(UserDataBaseList)

# GUI:
root = Tk()
root.title("Hire now")

frame=Frame(root, height=100)
frame.grid(row=0, column=0, sticky=N+S+E+W)

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