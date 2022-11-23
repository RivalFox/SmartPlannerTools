from email import message
import getpass
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os.path
import tkinter as tk


name = ""
stdID = ""
crHrs = ""
choiceList = []
inputFile = ""


def GUI():
	# create root window
	root = Tk()
	# root window title and dimension
	root.title("Welcome to Smart Planner Tool")
	# Set geometry(widthxheight)
	root.geometry('900x600')
	#root.configure(bg='#856ff8')
	lb_hi = Label(root, text="Welcome to Team3 Smart Planning Tool", font = ('calibre',15,'bold')).grid(row=0, column=1)
	#lb1 = Label(root, text="", font = ('calibre',10,'bold')).grid(row=4, column=0)
	lb1 = Label(root, text="Select Credit Hours:", font = ('calibre',10,'bold')).grid(row=4, column=0)
	lb2 = Label(root, text="Select Interest 1st:", font = ('calibre',10,'bold')).grid(row=5, column=0)
	lb2 = Label(root, text="Select Interest 2nd:", font = ('calibre',10,'bold')).grid(row=6, column=0)
	lb2 = Label(root, text="Select Interest 3rd:", font = ('calibre',10,'bold')).grid(row=7, column=0)


	name_var=tk.StringVar()
	stdID_var=tk.StringVar()
	inputFilePath = tk.StringVar()

	def show():
		
		name=name_var.get()
		stdID=stdID_var.get()
		crHrs= clicked0.get()
		choice1 = clicked1.get()
		choice2 = clicked2.get()
		choice3 = clicked3.get()
		inputFile = inputFilePath.get()

		stdName = Label (root,text=name).grid(row=9,column=1)
		ID = Label (root,text=stdID).grid(row=10,column=1)
		choice0 = Label(root,text=crHrs).grid(row=11,column=1)
		myChoice= Label (root, text=choice1).grid(row=12,column=1)
		myChoice= Label (root, text=choice2).grid(row=13,column=1)
		myChoice= Label (root, text=choice3).grid(row=14,column=1)
		selectedInput= Label(root, text=inputFile).grid(row=15,column=1)
	 
		#print in command line
		print("The name is : " + name)
		print("The password is : " + stdID)
		print("User selected credit hours: " +crHrs)
		print("User selected 1st interest: " +choice1)
		print("User selected 2nd interest: " +choice2)
		print("User selected 3rd interest: " +choice3)
		print("Selected input file path: " +inputFile)
		
###################################################################################
	# creating a label for
	# name using widget Label
	name_label = tk.Label(root, text = 'Name:', font=('calibre',10, 'bold'))
	# creating a entry for input
	# name using widget Entry
	name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')) 
	# creating a label for password
	stdID_label = tk.Label(root, text = 'Student ID:', font = ('calibre',10,'bold')) 
	# creating a entry for password
	stdID_entry=tk.Entry(root, textvariable = stdID_var, font = ('calibre',10,'normal'))
	#passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*') 
	# placing the label and entry in
	# the required position using grid
	# method
	name_label.grid(row=2,column=0)
	name_entry.grid(row=2,column=1)
	stdID_label.grid(row=3,column=0)
	stdID_entry.grid(row=3,column=1)


	#################################
	
	optCreditHrs =[
		"Full-time",
		"Three quarter-time",
		"Half-time",
		"Less than half-time"
		]

	###############################################
	optionsInterests1 =[
		"None",
		"Psychology", 
		"Journalism", 
		"Statistics", 
		"Kinesiology", 
		"Geology", 
		"Art History", 
		"Finance"
		]

	optionsInterests2 =[
		"None",
		"Psychology", 
		"Journalism", 
		"Statistics", 
		"Kinesiology", 
		"Geology", 
		"Art History", 
		"Finance"
		]

	optionsInterests3 =[
		"None",
		"Psychology", 
		"Journalism", 
		"Statistics", 
		"Kinesiology", 
		"Geology", 
		"Art History", 
		"Finance"
		]

	##https://pythonguides.com/python-tkinter-grid/####
	#This website shows how to use grid
	#########Credit Hours######################
	clicked0 = StringVar()
	clicked0.set(optCreditHrs[0])
	drop0= OptionMenu(root, clicked0, *optCreditHrs)
	#drop1.grid(sticky = 'E',row=4,column=1,columnspan = 1)
	drop0.grid(row=4,column=1)

	############Interest1######################
	clicked1 = StringVar()
	clicked1.set(optionsInterests1[0])
	drop1= OptionMenu(root, clicked1, *optionsInterests1)
	#drop1.grid(sticky = 'E',row=4,column=1,columnspan = 1)
	drop1.grid(row=5,column=1)

	############Interest2######################
	clicked2 = StringVar()
	clicked2.set(optionsInterests2[0])
	drop2= OptionMenu(root, clicked2, *optionsInterests2)
	drop2.grid(row=6,column=1)
	###########################################

	############Interest3######################
	clicked3 = StringVar()
	clicked3.set(optionsInterests3[0])
	drop3= OptionMenu(root, clicked3, *optionsInterests3)
	drop3.grid(row=7,column=1)
	###########################################

	# return the file path
	def select_file():
		# used to get to the proper directory
		osUser = getpass.getuser()
		# file types displayed in file explorer
		filetypes = (
			('All files', '*.*'), ('text files', "*.txt"), ('PDF Document', '*.pdf')
		)
		# returns path of selected file
		filename = fd.askopenfilename(initialdir='C:/Users/%s/Documents' % osUser, filetypes=filetypes)
		# split the filepath to get the directory 
		#directory = os.path.split(filename)[0]
		#print(directory)
		#inputFilePath.set(directory+filename)
		inputFilePath.set(filename)

	# open button for file dialog
	open_button = ttk.Button(root, text = 'Input Files', command = select_file)
	open_button.grid(row = 8, column = 1)

	###########################################
	showSelected = Button(root, text= "Show Selected", command =show).grid(row=19,column=1)

	#submitButton = Button(root, text= "Submit", command=executedProg).grid(sticky=S)
	###########################################

	#strChoice= clicked.get()
	root.mainloop()

	name=name_var.get()
	stdID=stdID_var.get()
	crHrs= clicked0.get()
	choice1 = clicked1.get()
	choice2 = clicked2.get()
	choice3 = clicked3.get()
	inputFile = inputFilePath.get()

	return name, stdID, crHrs, choice1, choice2, choice3, inputFile


