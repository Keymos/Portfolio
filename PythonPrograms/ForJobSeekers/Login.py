from tkinter import *
from tkinter import ttk



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

Button_Login = Button(frame, text='Log In', padx=5)#, command=insert_week)
Button_Login.grid(row=0, column=2, columnspan=2)

Button_Register = Button(frame, text='Register')#, command=insert_week)
Button_Register.grid(row=1, column=2, columnspan=2)

root.mainloop()