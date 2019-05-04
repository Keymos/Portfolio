from tkinter import *
from tkinter import ttk




def GridForget():
	Emptyfield.grid_forget()

def Grid_AddJobOffer_Show():
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



root = Tk()
root.title("Hire now !")


frame = Frame(root)
frame.grid(row=0, column=0)

Button_AddJobOffer = Button(frame, text='Add Job Offer', width=25, command=Grid_AddJobOffer_Show)
Button_AddJobOffer.grid(row=0, column=0)
Button_BrowseJobOffers = Button(frame, text='Browse Job Offers', width=25)
Button_BrowseJobOffers.grid(row=0, column=1)
Button_DeleteJobOffer = Button(frame, text='Delete Job Offer', width=25)
Button_DeleteJobOffer.grid(row=0, column=2)
Button_BrowseListOfJobSeekers = Button(frame, text='Browse List Of Job Seekers', width=25)
Button_BrowseListOfJobSeekers.grid(row=0, column=3)
Emptyfield = Label(frame, height=32)
Emptyfield.grid(row=1)


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

# Frame_AddJobOffer.grid_forget()

root.mainloop()