#----------------------------------------------------------------------#
# main.py
7#  
# This class is used to manage the application.
# 
# Rachel Mailach
#----------------------------------------------------------------------#

from Tkinter import *
import simulation
import guiInput
import guiOutput

class MyWindow(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)	# Because GUIs are hierarchical, it is a good idea to keep track of parent widgets
		self.parent = parent		# reference to parent
		self.initialize()

	def initialize(self):		
		#self.process = simulation.Model()		

		# create the input frame
		self.frameIn = guiInput.Input(self)
		self.frameIn.grid(row = 0, column = 0, padx = 5, pady =5, ipadx = 5, ipady = 5)

		# create the output frame
		self.frameOut = guiOutput.Output(self)
		self.frameOut.grid(row = 1, column = 0, padx = 5, pady =5, ipadx = 5, ipady = 5)

		# bind simulate button
		self.bind("<<input_simulate>>", self.submit)
	
	def submit(self, event):
		simulation.Run(self)
		self.frameOut.GetOutputList()


	

def main():
	window = MyWindow(None)				# instantiate the class with no parent (None)
	window.title('Discrete Event Simulation')	# title the window	
	#window.geometry("500x600")			# set window size
	window.mainloop()							# loop indefinitely, wait for events


if __name__ == '__main__': main()

