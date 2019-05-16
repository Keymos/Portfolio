from tkinter import *
from tkinter import ttk
import os



def Index_LoadAllJobOffersIDs():
	global AllJobsList
	AllJobsList = os.listdir("./List Of Jobs/")
	print(len(AllJobsList))
	j = 0
	while j < len(AllJobsList):
		AllJobsList[j] = AllJobsList[j].strip('.txt')
		j += 1

Index_LoadAllJobOffersIDs()

def GetJobNameFrom_Index_LoadAllJobOffersIDs(JobSeekerid):
	# Jobid is a string
	JobSeekerfile = open('./List Of Jobs/%s.txt'% JobSeekerid, 'r')
	x = JobSeekerfile.readline().strip('\n')
	JobSeekerfile.close()
	return x

def ShowAllJObs():
	AllJobOffers_Textfield.delete('1.0', 'end')
	i = len(AllJobsList)
	while i != 0:
		AllJobOffers_Textfield.insert('1.0', '%s ------ %s\n'%(AllJobsList[i-1], GetJobNameFrom_Index_LoadAllJobOffersIDs(AllJobsList[i-1])), 'tag %s'%AllJobsList[i-1])
		i = i - 1

def Index_LoadAllJobOffersIDs():
	global AllJobsList
	AllJobsList = os.listdir("./List Of Jobs/")
	print(len(AllJobsList))
	j = 0
	while j < len(AllJobsList):
		AllJobsList[j] = AllJobsList[j].strip('.txt')
		j += 1

def clearAllfields():
	CompanyInformationName.delete('1.0', 'end')
	CompanyInformationAdress.delete('1.0', 'end')
	CompanyInformationPhone.delete('1.0', 'end')
	CompanyInformationEmail.delete('1.0', 'end')
	Degree.delete('1.0', 'end')
	Qualification.delete('1.0', 'end')
	Experience.delete('1.0', 'end')
	Mission.delete('1.0', 'end')




def Grid_AddJobOffer_Show():
	scrollbar.grid_forget()
	Frame_AddJobOffer.grid_forget()
	UserID_Label.grid_forget()
	updateUserInfo_Botton.grid_forget()
	AllJobOffers_Textfield.grid_forget()
	SearchButton2.grid(row=0, column=1, sticky=E)
	ApplyForJob_Button.grid(row=0, column=2, sticky=W)
	Frame_AddJobOffer.grid(row=1, columnspan=4)
	AddJobOffer_JobID_Label.grid(row=0, column=0)
	AddJobOffer_JobID.grid(row=0, column=1, sticky=W)
	CompanyInformation_Label.grid(row=1, column=0, columnspan=4, sticky=W)
	CompanyInformationName_Label.grid(row=2, column=0)
	CompanyInformationName.grid(row=2, column=1, columnspan=3)
	CompanyInformationAdress_Label.grid(row=3, column=0)
	CompanyInformationAdress.grid(row=3, column=1, columnspan=3)
	CompanyInformationPhone_Label.grid(row=4, column=0)
	CompanyInformationPhone.grid(row=4, column=1, columnspan=3)
	CompanyInformationEmail_Label.grid(row=5, column=0)
	CompanyInformationEmail.grid(row=5, column=1, columnspan=3)
	RequestedProfileDescription_Label.grid(row=6, column=0, columnspan=4, sticky=W)
	Degree_Label.grid(row=7, column=0)
	Degree.grid(row=7, column=1, columnspan=3)
	Qualification_Label.grid(row=8, column=0)
	Qualification.grid(row=8, column=1, columnspan=3)
	Experience_Label.grid(row=9, column=0)
	Experience.grid(row=9, column=1, columnspan=3)
	Mission_Label.grid(row=10, column=0)
	Mission.grid(row=10, column=1, columnspan=3)

def SearchJobOffer():
	x = (AddJobOffer_JobID.get('1.0', 'end').strip('\n')).zfill(8)
	if x in AllJobsList:
		x = open('./List of Jobs/%s.txt' % x, 'r')
		z = x.read().strip('\n')
		y = z.split('\n>>>')
		# print(y)
		clearAllfields()
		CompanyInformationName.insert('1.0', y[0])
		CompanyInformationAdress.insert('1.0', y[1])
		CompanyInformationPhone.insert('1.0', y[2])
		CompanyInformationEmail.insert('1.0', y[3])
		Degree.insert('1.0', y[4])
		Qualification.insert('1.0', y[5])
		Experience.insert('1.0', y[6])
		Mission.insert('1.0', y[7])
	else:
		print('bzz')

def ShowUserInformation():
	CurrentUserFile = open("CurrentUserFile.txt", 'r')
	CurrentUSerId = CurrentUserFile.readline().split(']')[1]
	x = CurrentUSerId.zfill(8)
	x = open('./List of Jobs/%s.txt' % x, 'r')
	z = x.read().strip('\n')
	y = z.split('\n>>>')
	# print(y)
	clearAllfields()
	CompanyInformationName.insert('1.0', y[0])
	CompanyInformationAdress.insert('1.0', y[1])
	CompanyInformationPhone.insert('1.0', y[2])
	CompanyInformationEmail.insert('1.0', y[3])
	Degree.insert('1.0', y[4])
	Qualification.insert('1.0', y[5])
	Experience.insert('1.0', y[6])
	Mission.insert('1.0', y[7])



def Grid_BrowseAndUpdate_Show():
	SearchButton2.grid_forget()
	Frame_AddJobOffer.grid_forget()
	AllJobOffers_Textfield.grid(row=1, column=0, columnspan=3, sticky=W)
	scrollbar.grid(row=1, column=2, sticky=S+N+E)

def Grid_UpdateJobSekkerInformation_Show():
	ShowUserInformation()
	clearAllfields()
	AllJobOffers_Textfield.grid_forget()
	scrollbar.grid_forget()
	updateUserInfo_Botton.grid(row=0, column=1, sticky=E)
	ApplyForJob_Button.grid_forget()
	SearchButton2.grid_forget()
	Frame_AddJobOffer.grid_forget()
	Frame_AddJobOffer.grid(row=1, columnspan=4)
	UserID_Label.grid(row=0, column=0)
	AddJobOffer_JobID.grid(row=0, column=1, sticky=W)
	CompanyInformation_Label.grid(row=1, column=0, columnspan=4, sticky=W)
	CompanyInformationName_Label.grid(row=2, column=0)
	CompanyInformationName.grid(row=2, column=1, columnspan=3)
	CompanyInformationAdress_Label.grid(row=3, column=0)
	CompanyInformationAdress.grid(row=3, column=1, columnspan=3)
	CompanyInformationPhone_Label.grid(row=4, column=0)
	CompanyInformationPhone.grid(row=4, column=1, columnspan=3)
	CompanyInformationEmail_Label.grid(row=5, column=0)
	CompanyInformationEmail.grid(row=5, column=1, columnspan=3)
	RequestedProfileDescription_Label.grid(row=6, column=0, columnspan=4, sticky=W)
	Degree_Label.grid(row=7, column=0)
	Degree.grid(row=7, column=1, columnspan=3)
	Qualification_Label.grid(row=8, column=0)
	Qualification.grid(row=8, column=1, columnspan=3)
	Experience_Label.grid(row=9, column=0)
	Experience.grid(row=9, column=1, columnspan=3)
	Mission_Label.grid(row=10, column=0)
	Mission.grid(row=10, column=1, columnspan=3)



root = Tk()
root.title("Hire now !")

frame = Frame(root)
frame.grid(row=0, column=0)

Button_SearchJobOffer = Button(frame, text='Search Job Offer', width=25, command=Grid_AddJobOffer_Show)
Button_SearchJobOffer.grid(row=0, column=0)
Button_BrowseJobOffers = Button(frame, text='Browse Job Offers', width=25, command=Grid_BrowseAndUpdate_Show)
Button_BrowseJobOffers.grid(row=0, column=1)
Button_UpdateInfo = Button(frame, text='Update Information', width=25, command=Grid_UpdateJobSekkerInformation_Show)
Button_UpdateInfo.grid(row=0, column=2)
Emptyfield = Label(frame, height=32)
Emptyfield.grid(row=1)

Frame_AddJobOffer = Frame(frame)

AddJobOffer_JobID_Label = Label(Frame_AddJobOffer, text="Job ID")
AddJobOffer_JobID = Text(Frame_AddJobOffer, height=1, width=25)

UserID_Label = Label(Frame_AddJobOffer, text="User ID")

CompanyInformation_Label = Label(Frame_AddJobOffer, text="User Information:")
CompanyInformationName_Label = Label(Frame_AddJobOffer, text="Name:")
CompanyInformationName = Text(Frame_AddJobOffer, height=1, width=50)
CompanyInformationAdress_Label = Label(Frame_AddJobOffer, text="Adress:")
CompanyInformationAdress = Text(Frame_AddJobOffer, height=1, width=50)
CompanyInformationPhone_Label = Label(Frame_AddJobOffer, text="Phone:")
CompanyInformationPhone = Text(Frame_AddJobOffer, height=1, width=50)
CompanyInformationEmail_Label = Label(Frame_AddJobOffer, text="Email:")
CompanyInformationEmail = Text(Frame_AddJobOffer, height=1, width=50)

RequestedProfileDescription_Label = Label(Frame_AddJobOffer, text="Profile Description:")
Degree_Label = Label(Frame_AddJobOffer, text="Degree:")
Degree = Text(Frame_AddJobOffer, height=5, width=50)
Qualification_Label = Label(Frame_AddJobOffer, text="Qualification:")
Qualification = Text(Frame_AddJobOffer, height=5, width=50)
Experience_Label = Label(Frame_AddJobOffer, text="Experience:")
Experience = Text(Frame_AddJobOffer, height=5, width=50)
Mission_Label = Label(Frame_AddJobOffer, text="Mission:")
Mission = Text(Frame_AddJobOffer, height=5, width=50)

SearchButton2 = Button(Frame_AddJobOffer, text="Search", command=SearchJobOffer)
ApplyForJob_Button = Button(Frame_AddJobOffer, text="Apply")
updateUserInfo_Botton = Button(Frame_AddJobOffer, text="Update")


scrollbar = Scrollbar(frame)

AllJobOffers_Textfield = Text(frame, width=66, height=30, yscrollcommand=scrollbar.set)
i = len(os.listdir('List of Jobs'))-1
while i != -1:
	file = open('List of Jobs/%s' % os.listdir('List of Jobs')[i])
	jobname = file.readline()
	AllJobOffers_Textfield.insert('1.0', '%s ------ %s\n'%(str(os.listdir('List of Jobs')[i]).zfill(8).strip('.txt'), jobname))
	i = i - 1
scrollbar.config(command=AllJobOffers_Textfield.yview)


root.mainloop()
