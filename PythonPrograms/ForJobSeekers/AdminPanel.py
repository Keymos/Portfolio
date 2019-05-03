from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hire now !")


Button_AddJobOffer = Button(root, text='Add Job Offer', width=25)
Button_AddJobOffer.grid(row=0, column=0)
Button_BrowseJobOffers = Button(root, text='Browse Job Offers', width=25)
Button_BrowseJobOffers.grid(row=0, column=1)
Button_DeleteJobOffer = Button(root, text='Delete Job Offer', width=25)
Button_DeleteJobOffer.grid(row=0, column=2)
Button_BrowseListOfJobSeekers = Button(root, text='Browse List Of Job Seekers', width=25)
Button_BrowseListOfJobSeekers.grid(row=0, column=3)



root.mainloop()