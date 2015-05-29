#----------------------------------------------------------------------#
# guiOutput.py
#  
# This class is used as a graphical user interface for a larger
# application.
# 
# Rachel Mailach
#----------------------------------------------------------------------#
from Tkinter import *
import ttk
import simulation


class Output(LabelFrame):
	def __init__(self, parent):
		LabelFrame.__init__(self, parent, text = "Output")	
		
		emptyLabel = Label(self, text = "")
		emptyLabel.pack()

		#self.rho = StringVar()
	
	def GetOutputList(self):
		#grab all output values
		CalcOutputList = simulation.CalcOutputList()
		SimOutputList = simulation.SimOutputList()		

		#create new frame within Output frame for calculated values
		f = Frame(self, width = 700, height = 700)
		f.pack(side=LEFT, expand = 1)
		
		mmkLabel = Label(f, text="For an M/M/k queue").grid(row=0, columnspan = 2)
		labels = ['utilization','pi_0','response time','time queued','number of jobs','number of jobs queued']
		r=1
		for elem in labels:
			Label(f, text=elem).grid(row=r, column=0)
			r=r+1
		r=1
		for i in CalcOutputList:
			Label(f, text=i, relief=SUNKEN, width=20).grid(row=r, column=1)
			r=r+1

		#create new frame within Output frame for simulated values
		f2 = Frame(self, width = 700, height = 700)
		f2.pack(side=RIGHT, expand = 1)
	
		simLabel = Label(f2, text="Simulated values").grid(row=0, columnspan=2)
		simLabels = ['Average time in system', 'Average time in queue'] #'Average number in the system', 'Average time in the system', 'Actual average service-time']
		r=1
		for elem in simLabels:
			Label(f2, text=elem).grid(row=r, column=0)
			r=r+1
		r=1
		for elem in SimOutputList:
			Label(f2, text=elem, relief=SUNKEN, width=20).grid(row=r, column=1)
			r=r+1

