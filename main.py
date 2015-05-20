#----------------------------------------------------------------------#
# main.py
#  
# This class is used to manage the application.
# 
# Rachel Mailach
#----------------------------------------------------------------------#

from Tkinter import *
import simulation
import gui

class MyWindow(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)	# Because GUIs are hierarchical, it is a good idea to keep track of parent widgets
		self.parent = parent		# reference to parent
		self.initialize()

	def initialize(self):		
		self.process = simulation.Model()		

		# create the input frame
		self.frameIn = gui.Input(self)
		self.frameIn.grid(row = 0, column = 0, padx = 5, pady =5, ipadx = 5, ipady = 5)

		# create the output frame
		self.frameOut = gui.Output(self)
		self.frameOut.grid(row = 1, column = 0, padx = 5, pady =5, ipadx = 5, ipady = 5)

		# bind simulate button
		self.bind("<<input_simulate>>", self.submit)
	
	def GetList(self):
		print "getlist from MAIN"
		var = gui.Input(self)
		return var.CreateList()
	
	def submit(self, event):
		print "submit method"
#		self.frameOut.GetList()
		self.process.Run()
        #value = self.frameIn.getValue()
        #result = self.process.addValue(value)
        #self.frameOut.outputText.set(result)


	

def main():
	window = MyWindow(None)						# instantiate the class with no parent (None)
	window.title('Discrete Event Simulation')	# title the window	
	#window.geometry("500x600")					# set window size
	window.mainloop()							# loop indefinitely, wait for events


if __name__ == '__main__': main()

