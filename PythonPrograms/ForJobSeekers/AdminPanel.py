from tkinter import *
from tkinter import ttk
import os


'''
What's left to be done:
	The search all job seekers thing
	Job seekers' back end.
'''













def clearAllfields():
	CompanyInformationName.delete('1.0', 'end')
	CompanyInformationAdress.delete('1.0', 'end')
	CompanyInformationPhone.delete('1.0', 'end')
	CompanyInformationEmail.delete('1.0', 'end')
	Degree.delete('1.0', 'end')
	Qualification.delete('1.0', 'end')
	Experience.delete('1.0', 'end')
	Mission.delete('1.0', 'end')





def Index_LoadAllJobSeekersIDs():
	global AllJobSeekersList
	AllJobSeekersList = os.listdir("./List Of JobSeekers/")
	print(len(AllJobSeekersList))
	j = 0
	while j < len(AllJobSeekersList):
		AllJobSeekersList[j] = AllJobSeekersList[j].strip('.txt')
		j += 1

Index_LoadAllJobSeekersIDs()


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
	JobSeekerfile = open('./List Of JobSeekers/%s.txt'% JobSeekerid, 'r')
	x = JobSeekerfile.readline().strip('\n')
	JobSeekerfile.close()
	return x






global JobID
def AddJob():
	try:
		JobID = int(str(AddJobOffer_JobID.get('1.0', END)).strip('\n'))
		JobID = str(JobID).zfill(8)
		if JobID in AllJobsList:
			print('bzz')
		else:
			x = open('./List of Jobs/%s.txt' % JobID, 'a+')
			x.write(CompanyInformationName.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + CompanyInformationAdress.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + CompanyInformationPhone.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + CompanyInformationEmail.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + Degree.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + Qualification.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + Experience.get('1.0', 'end').strip('\n'))
			x.write("\n>>>" + Mission.get('1.0', 'end').strip('\n'))
			x.close()
			Index_LoadAllJobOffersIDs()
	except ValueError:
		print("The input was not a valid integer.")


def DeleteJob():
	x = (SearchJobID.get('1.0', 'end').strip('\n')).zfill(8)
	print(x)
	if x in AllJobsList:
		os.remove('./List of Jobs/%s.txt' % x)
		AllJobsList.remove(x)


def SearchJobOffer():
	if (SearchJobID.get('1.0', 'end').strip('\n')) != '':
		x = (SearchJobID.get('1.0', 'end').strip('\n')).zfill(8)
	else:
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


def ShowAllJobSeekers():
	i = len(AllJobSeekersList)
	while i != 0:
		AllJobSeekers_Textfield.insert('1.0', '%s ------ %s\n'%(AllJobSeekersList[i-1], GetJobNameFrom_Index_LoadAllJobOffersIDs(AllJobSeekersList[i-1])), 'tag %s'%AllJobSeekersList[i-1])
		i = i - 1











def Grid_AddJobOffer_Show():
	clearAllfields()
	scrollbar.grid_forget()
	AllJobSeekers_Textfield.grid_forget()
	Frame_BrowseAndUpdate.grid_forget()
	Frame_SearchJobSeekers.grid_forget()
	SearchJob_SearchButton.grid_forget()
	SearchButton2.grid_forget()
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
	AddjobButton2.grid(row=0, column=1, sticky=E)

def Grid_BrowseAndUpdate_Show():
	AddjobButton2.grid_forget()
	scrollbar.grid_forget()
	AllJobSeekers_Textfield.grid_forget()
	DeleteJobOfferButton.grid_forget()
	Frame_BrowseAndUpdate.grid_forget()
	Frame_AddJobOffer.grid_forget()
	Frame_SearchJobSeekers.grid_forget()
	Frame_BrowseAndUpdate.grid(row=1, columnspan=4)
	SearchJobID_Label.grid(row=0, column=0, sticky=W)
	SearchJobID.grid(row=0, column=1, columnspan=3)
	SearchJob_SearchButton.grid(row=0, column=4)

def SearchJob():
	scrollbar.grid_forget()
	AllJobSeekers_Textfield.grid_forget()
	Grid_AddJobOffer_Show()
	SearchButton2.grid(row=0, column=1, sticky=E)
	AddjobButton2.grid_forget()
	SearchJobOffer()
	SearchJobID.delete('1.0', 'end')
	AddJobOffer_JobID.delete('1.0', 'end')


def Grid_DeleteJobOffer_Show():
	scrollbar.grid_forget()
	AllJobSeekers_Textfield.grid_forget()
	Frame_AddJobOffer.grid_forget()
	SearchJob_SearchButton.grid_forget()
	Frame_SearchJobSeekers.grid_forget()
	Frame_BrowseAndUpdate.grid(row=1, columnspan=4)
	SearchJobID_Label.grid(row=0, column=0, sticky=W)
	SearchJobID.grid(row=0, column=1, columnspan=3)
	DeleteJobOfferButton.grid(row=0, column=4)

def Grid_SearchJobSeekers_Show():
	scrollbar.grid_forget()
	AllJobSeekers_Textfield.grid_forget()
	DeleteJobOfferButton.grid_forget()
	Frame_BrowseAndUpdate.grid_forget()
	Frame_AddJobOffer.grid_forget()
	Frame_SearchJobSeekers.grid(row=1, columnspan=4)
	SearchBy_Label.grid(row=1, column=0)
	SearchAll_Button.grid(row=2, column=0)
	SearchByJobOfferAppliedTo_Button.grid(row=2, column=1)
	SearchByJob_TextField.grid(row=2, column=2)

def Grid_BrowseAllJobSeekers_Show():
	ShowAllJobSeekers()
	AllJobSeekers_Textfield.grid(row=1, column=0, columnspan=4, sticky=W)
	scrollbar.grid(row=1, column=3, sticky=S+N+E)
	print("bzz")

def ShowJobSeekersByJobs():
	JobSeekersAppliedToJob_List =[]
	JobIDAppliedTo = SearchByJob_TextField.get('1.0', 'end').strip('\n').zfill(8)
	print('jobappliedto' + JobIDAppliedTo)
	for currentFile in os.listdir('List of JobSeekers'):
		TempFile = open('List of JobSeekers/%s' % currentFile, 'r')
		counter = 0
		while counter < 8:
			TempFile.readline()
			counter += 1
		HajaHasilou = TempFile.readline().strip('>>> ')
		print('JobIDAppliedTo' + JobIDAppliedTo)
		if int(JobIDAppliedTo) == int(HajaHasilou):
			print('bouf' + currentFile)
			JobSeekersAppliedToJob_List.append(currentFile.strip('.txt'))
		print(JobSeekersAppliedToJob_List)
	i = len(JobSeekersAppliedToJob_List)
	while i != 0:
		AllJobSeekers_Textfield.insert('1.0', '%s'%(JobSeekersAppliedToJob_List[i-1]))
		i = i - 1

	Grid_BrowseAllJobSeekers_Show()






















root = Tk()
root.title("Hire now !")

frame = Frame(root)
frame.grid(row=0, column=0)

Button_AddJobOffer = Button(frame, text='Add Job Offer', width=25, command=Grid_AddJobOffer_Show)
Button_AddJobOffer.grid(row=0, column=0)
Button_BrowseJobOffers = Button(frame, text='Browse Job Offers', width=25, command=Grid_BrowseAndUpdate_Show)
Button_BrowseJobOffers.grid(row=0, column=1)
Button_DeleteJobOffer = Button(frame, text='Delete Job Offer', width=25, command=Grid_DeleteJobOffer_Show)
Button_DeleteJobOffer.grid(row=0, column=2)
Button_BrowseListOfJobSeekers = Button(frame, text='Browse List Of Job Seekers', width=25, command=Grid_SearchJobSeekers_Show)
Button_BrowseListOfJobSeekers.grid(row=0, column=3)
Emptyfield = Label(frame, height=32)
Emptyfield.grid(row=1)

# AddJobOffer
Frame_AddJobOffer = Frame(frame)

AddJobOffer_JobID_Label = Label(Frame_AddJobOffer, text="Job ID")
AddJobOffer_JobID = Text(Frame_AddJobOffer, height=1, width=25)

CompanyInformation_Label = Label(Frame_AddJobOffer, text="Company Information:")
CompanyInformationName_Label = Label(Frame_AddJobOffer, text="Name:")
CompanyInformationName = Text(Frame_AddJobOffer, height=1, width=75)
CompanyInformationAdress_Label = Label(Frame_AddJobOffer, text="Adress:")
CompanyInformationAdress = Text(Frame_AddJobOffer, height=1, width=75)
CompanyInformationPhone_Label = Label(Frame_AddJobOffer, text="Phone:")
CompanyInformationPhone = Text(Frame_AddJobOffer, height=1, width=75)
CompanyInformationEmail_Label = Label(Frame_AddJobOffer, text="Email:")
CompanyInformationEmail = Text(Frame_AddJobOffer, height=1, width=75)

RequestedProfileDescription_Label = Label(Frame_AddJobOffer, text="Requested Profile Description:")
Degree_Label = Label(Frame_AddJobOffer, text="Degree:")
Degree = Text(Frame_AddJobOffer, height=5, width=75)
Qualification_Label = Label(Frame_AddJobOffer, text="Qualification:")
Qualification = Text(Frame_AddJobOffer, height=5, width=75)
Experience_Label = Label(Frame_AddJobOffer, text="Experience:")
Experience = Text(Frame_AddJobOffer, height=5, width=75)
Mission_Label = Label(Frame_AddJobOffer, text="Mission:")
Mission = Text(Frame_AddJobOffer, height=5, width=75)

SearchButton2 = Button(Frame_AddJobOffer, text="Search", command=SearchJob)
AddjobButton2 = Button(Frame_AddJobOffer, text="Add", command=AddJob)


# Browse and update
Frame_BrowseAndUpdate = Frame(frame)

SearchJobID_Label = Label(Frame_BrowseAndUpdate, text="Job ID:")
SearchJobID = Text(Frame_BrowseAndUpdate, height=1, width=25)
SearchJob_SearchButton = Button(Frame_BrowseAndUpdate, text="Search", command=SearchJob)

DeleteJobOfferButton = Button (Frame_BrowseAndUpdate, text="Delete", command=DeleteJob)

Frame_SearchJobSeekers = Frame(frame)
SearchBy_Label = Label(Frame_SearchJobSeekers, text="Search by:")
SearchAll_Button = Button(Frame_SearchJobSeekers, text="All", command=Grid_BrowseAllJobSeekers_Show)
SearchByJobOfferAppliedTo_Button = Button(Frame_SearchJobSeekers,text="Search by job ID:", command=ShowJobSeekersByJobs)
SearchByJob_TextField = Text(Frame_SearchJobSeekers, height=1, width=25)


scrollbar = Scrollbar(frame)

AllJobSeekers_Textfield = Text(frame, width=90, height=30, yscrollcommand=scrollbar.set)


scrollbar.config(command=AllJobSeekers_Textfield.yview)

root.mainloop()