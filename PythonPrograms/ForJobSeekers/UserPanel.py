from tkinter import *
from tkinter import ttk


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


def Grid_BrowseAndUpdate_Show():
	SearchButton2.grid_forget()
	Frame_AddJobOffer.grid_forget()
	AllJobOffers_Textfield.grid(row=1, column=0, columnspan=3, sticky=W)
	scrollbar.grid(row=1, column=2, sticky=S+N+E)

def Grid_UpdateJobSekkerInformation_Show():
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

CompanyInformation_Label = Label(Frame_AddJobOffer, text="Company Information:")
CompanyInformationName_Label = Label(Frame_AddJobOffer, text="Name:")
CompanyInformationName = Text(Frame_AddJobOffer, height=1, width=50)
CompanyInformationAdress_Label = Label(Frame_AddJobOffer, text="Adress:")
CompanyInformationAdress = Text(Frame_AddJobOffer, height=1, width=50)
CompanyInformationPhone_Label = Label(Frame_AddJobOffer, text="Phone:")
CompanyInformationPhone = Text(Frame_AddJobOffer, height=1, width=50)
CompanyInformationEmail_Label = Label(Frame_AddJobOffer, text="Email:")
CompanyInformationEmail = Text(Frame_AddJobOffer, height=1, width=50)

RequestedProfileDescription_Label = Label(Frame_AddJobOffer, text="Requested Profile Description:")
Degree_Label = Label(Frame_AddJobOffer, text="Degree:")
Degree = Text(Frame_AddJobOffer, height=5, width=50)
Qualification_Label = Label(Frame_AddJobOffer, text="Qualification:")
Qualification = Text(Frame_AddJobOffer, height=5, width=50)
Experience_Label = Label(Frame_AddJobOffer, text="Experience:")
Experience = Text(Frame_AddJobOffer, height=5, width=50)
Mission_Label = Label(Frame_AddJobOffer, text="Mission:")
Mission = Text(Frame_AddJobOffer, height=5, width=50)

SearchButton2 = Button(Frame_AddJobOffer, text="Search")#, command=SearchJob)
ApplyForJob_Button = Button(Frame_AddJobOffer, text="Apply")
updateUserInfo_Botton = Button(Frame_AddJobOffer, text="Update")


scrollbar = Scrollbar(frame)

AllJobOffers_Textfield = Text(frame, width=66, height=30, yscrollcommand=scrollbar.set)
AllJobOffers_Textfield.insert('1.0', "Job 1 \n", "line1", "line 2  ", "line2", "\nwhatever", "line3")
AllJobOffers_Textfield.tag_config("line1", foreground="blue")

scrollbar.config(command=AllJobOffers_Textfield.yview)


root.mainloop()
