#----------------------------------------------------------------------#
# guiInput.py
#  
# This class is used as a graphical user interface for a larger
# application.
# 
# Rachel Mailach
#----------------------------------------------------------------------#
from Tkinter import *
import ttk

class Input(LabelFrame):
	valuesList = []
	distList = []
#	List = []

	def __init__(self, parent):
		LabelFrame.__init__(self, parent, text = "Input")

		self.inputEntry_1 = IntVar()
		self.inputEntry_2 = DoubleVar()
		self.inputEntry_3 = DoubleVar()
		self.inputEntry_4 = DoubleVar()
		self.inputEntry_5 = DoubleVar()
		self.inputEntry_6 = DoubleVar()
		self.inputEntry_7 = DoubleVar()
		self.inputEntry_8 = DoubleVar()

		# create widgets, parent = self because window is parent
		# Labels
		self.numServers = Label(self, text = "number of servers")	# number of servers
		self.arrivalRate = Label(self, text = u'\u03bb')			# lambda
		self.serviceRate = Label(self, text = u'\u03bc')			# mu
		self.turnonTime = Label(self, text = "turn-on time")		# turn-on time
		self.jobThreshold = Label(self, text = "k")					# k
		self.turnoffRate = Label(self, text = u'\u03b1')			# alpha
		self.upStateRate = Label(self, text = u'\u0263')			# gamma
		self.simLength = Label(self, text = "simulation length")	# max sim time
		
		# Entry Boxes
		self.entry_1 = Entry(self, textvariable = self.inputEntry_1)
		self.entry_2 = Entry(self, textvariable = self.inputEntry_2)
		self.entry_3 = Entry(self, textvariable = self.inputEntry_3)
		self.entry_4 = Entry(self, textvariable = self.inputEntry_4)
		self.entry_5 = Entry(self, textvariable = self.inputEntry_5)
		self.entry_6 = Entry(self, textvariable = self.inputEntry_6)
		self.entry_7 = Entry(self, textvariable = self.inputEntry_7)
		self.entry_8 = Entry(self, textvariable = self.inputEntry_8)

		# Simulate Button
		self.simulateButton = Button(self, text = "SIMULATE", command = self.OnButtonClick)

		# Menu
		#dropDown = Menu(self)
		#self.config(menu = dropDown)
		#subMenu = Menu(dropDown)
		#dropDown.add_cascade(label = "Distribution", menu = subMenu)
		#subMenu.add_command(label = "Exponential", command = self.DropDown)
		#subMenu.add_separator()
		#subMenu.add_command(label = "Custom", command = self.DropDown)

		self.distributions = ('Select Distribution', 'Exponential', 'Normal', 'Custom')

		self.comboBox_1 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_1.current(0) # set selection

		self.comboBox_2 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_2.current(0) # set selection

		self.comboBox_3 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_3.current(0) # set selection

		self.comboBox_4 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_4.current(0) # set selection

#		self.comboBox_5 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
#		self.comboBox_5.current(0) # set selection

		# send to layout manager 
		self.numServers.grid(row = 0, column = 0)
		self.arrivalRate.grid(row = 1, column = 0)
		self.serviceRate.grid(row = 2, column = 0)
		self.turnonTime.grid(row = 3, column = 0)
		self.jobThreshold.grid(row = 0, column = 5)
		self.turnoffRate.grid(row = 1, column = 5)
		self.upStateRate.grid(row = 2, column = 5)
		self.simLength.grid(row = 3, column = 5)

		self.entry_1.grid(row = 0, column = 1)
		self.entry_2.grid(row = 1, column = 1)
		self.entry_3.grid(row = 2, column = 1)
		self.entry_4.grid(row = 3, column = 1)
		self.entry_5.grid(row = 0, column = 6)
		self.entry_6.grid(row = 1, column = 6)
		self.entry_7.grid(row = 2, column = 6)
		self.entry_8.grid(row = 3, column = 6)
		
		self.simulateButton.grid(row = 8, columnspan = 8)
	
		self.comboBox_1.grid(row = 1, column = 3)
		self.comboBox_2.grid(row = 2, column = 3)
		self.comboBox_3.grid(row = 1, column = 7)
		self.comboBox_4.grid(row = 2, column = 7)
	#	self.comboBox_5.grid(row = 1, column = 7)

	def OnButtonClick(self):
		self.GetNumericValues()
		self.GetDropDownValues()

		# send to submit button in main
		self.simulateButton.event_generate("<<input_simulate>>")

	def IsFloat(self, string):
		try:
			float(string)
			return True
		except ValueError:
			return False

	def GetNumericValues(self):
		value1 = self.inputEntry_1.get()
		value2 = self.inputEntry_2.get()
		value3 = self.inputEntry_3.get()
		value4 = self.inputEntry_4.get()
		value5 = self.inputEntry_5.get()
		value6 = self.inputEntry_6.get()
		value7 = self.inputEntry_7.get()
		value8 = self.inputEntry_8.get()

		if value1 == 0:	 print "Field 1 has to be non-zero"
		if value2 == 0.0: print "Field 2 has to be non-zero!"
		if value3 == 0.0: print "Field 3 has to be non-zero!"
#		if not self.IsFloat(value4): print "Field 4 has to be a number!"
#		if not self.IsFloat(value5): print "Field 5 has to be a number!"
#		if not self.IsFloat(value6): print "Field 6 has to be a number!"
#		if not self.IsFloat(value7): print "Field 7 has to be a number!"
		if value8 == 0.0: print "Field 8 has to be non-zero!"

		Input.valuesList = [value1, value2, value3, value4, value5, value6, value7, value8]
		return Input.valuesList
		
	def GetDropDownValues(self):
		if self.comboBox_1.get() == 'Select Distribution': print "Box 1 has to have a selection"
		if self.comboBox_2.get() == 'Select Distribution': print "Box 2 has to have a selection"
		if self.comboBox_3.get() == 'Select Distribution': print "Box 3 has to have a selection"
		if self.comboBox_4.get() == 'Select Distribution': print "Box 4 has to have a selection"
#		if self.comboBox_5.get() == 'Select Distribution': print "Box 5 has to have a selection"

		Input.distList = ["", self.comboBox_1.get(), self.comboBox_2.get(), "", "", self.comboBox_3.get(), self.comboBox_4.get(), ""]
		return Input.distList

	def CreateList(self):
		InputList = zip(Input.valuesList, Input.distList)
		return InputList