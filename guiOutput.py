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
		#self.pi_0 = StringVar()
		#self.rt = StringVar()
		#self.timeQueued = StringVar()
		#self.numJobs = StringVar()
		#self.numJobsQueued = StringVar()
	
	def GetOutputList(self):
		#grab all output values
		OutputList = simulation.CreateOutputList()
		
		#create new frame within Output frame
		f = Frame(self, width = 700, height = 700)
		f.pack(side=LEFT, expand = 1)
		
		mmkLabel = Label(f, text="For an M/M/k queue").grid(row=0, columnspan = 2)

		labels = ['utilization','pi_0','response time','time queued','number of jobs','number of jobs queued']
		r=1
		for elem in labels:
			Label(f, text=elem).grid(row=r, column=0)
			r=r+1
		r=1
		for i in OutputList:
			Label(f, text=i, relief=SUNKEN, width=20).grid(row=r, column=1)
			r=r+1

		#self.rho.set("utilization = " + str(OutputList[0]))
		#self.pi_0.set("pi_0 = "+ str(OutputList[1]))
		#self.rt.set("response time = "+ str(OutputList[2]))
		#self.timeQueued.set("time queued = " + str(OutputList[3]))
		#self.numJobs.set("number of jobs = "+ str(OutputList[4]))
		#self.numJobsQueued.set("number of jobs queued = "+ str(OutputList[5]))
		
		#self.rhoLabel = Label(self, textvariable = self.rho)
		#self.pi_0Label = Label(self, textvariable = self.pi_0)
		#self.rtLabel = Label(self, textvariable = self.rt)
		#self.timeQueuedLabel = Label(self, textvariable = self.timeQueued)
		#self.numJobsLabel = Label(self, textvariable = self.numJobs)
		#self.numJobsQueuedLabel = Label(self, textvariable = self.numJobsQueued)

		#self.rhoLabel.pack(fill=BOTH, expand=1)
		#self.pi_0Label.pack(fill=BOTH, expand=1)
		#self.rtLabel.pack(fill=BOTH, expand=1)
		#self.timeQueuedLabel.pack(fill=BOTH, expand=1)
		#self.numJobsLabel.pack(fill=BOTH, expand=1)
		#self.numJobsQueuedLabel.pack(fill=BOTH, expand=1)
		
