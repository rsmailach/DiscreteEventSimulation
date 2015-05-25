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

		self.pi_0 = StringVar()
	
	def GetOutputList(self):
		#grab all output values
		OutputList = simulation.CreateOutputList()
		self.pi_0.set("pi_0" + " = "+ str(OutputList))
		
		self.pi_0Label = Label(self, textvariable = self.pi_0)
		self.pi_0Label.pack()
		
