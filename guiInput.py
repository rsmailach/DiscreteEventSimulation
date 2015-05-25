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

# Define a class inherit from an exception type
class CustomError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg

class Input(LabelFrame):
	valuesList = []
	distList = []

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
		labels = ['number of servers', u'\u03bb', u'\u03bc', 'turn-on time', 'k', u'\u03b1', u'\u0263', 'simulation length']
		r=0
		c=0
		for elem in labels:
			Label(self, text=elem).grid(row=r, column=c)
			r=r+1
			if r > 3:
				r=0
				c=3
			
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

		self.distributions = ('Select Distribution', 'Exponential', 'Normal', 'Custom')

		self.comboBox_1 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_1.current(0) # set selection

		self.comboBox_2 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_2.current(0) # set selection

		self.comboBox_3 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_3.current(0) # set selection

		self.comboBox_4 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_4.current(0) # set selection

		self.entry_1.grid(row = 0, column = 1)
		self.entry_2.grid(row = 1, column = 1)
		self.entry_3.grid(row = 2, column = 1)
		self.entry_4.grid(row = 3, column = 1)
		self.entry_5.grid(row = 0, column = 4)
		self.entry_6.grid(row = 1, column = 4)
		self.entry_7.grid(row = 2, column = 4)
		self.entry_8.grid(row = 3, column = 4)
		
		self.simulateButton.grid(row = 8, columnspan = 6)
	
		self.comboBox_1.grid(row = 1, column = 2)
		self.comboBox_2.grid(row = 2, column = 2)
		self.comboBox_3.grid(row = 1, column = 5)
		self.comboBox_4.grid(row = 2, column = 5)


	def OnButtonClick(self):
		self.GetNumericValues()
		self.GetDropDownValues()

		# send to submit button in main
		self.simulateButton.event_generate("<<input_simulate>>")	
			

	def GetNumericValues(self):
		value1 = self.inputEntry_1.get()
		value2 = self.inputEntry_2.get()
		value3 = self.inputEntry_3.get()
		value4 = self.inputEntry_4.get()
		value5 = self.inputEntry_5.get()
		value6 = self.inputEntry_6.get()
		value7 = self.inputEntry_7.get()
		value8 = self.inputEntry_8.get()

		if value1 >= 0: print "Field 1 has to be non-zero"
		if value2 >= 0.0: print "Field 2 has to be non-zero!"
		if value3 >= 0.0: print "Field 3 has to be non-zero!"
#		if not self.IsFloat(value4): print "Field 4 has to be a number!"
#		if not self.IsFloat(value5): print "Field 5 has to be a number!"
#		if not self.IsFloat(value6): print "Field 6 has to be a number!"
#		if not self.IsFloat(value7): print "Field 7 has to be a number!"
		if value8 >= 0.0: print "Field 8 has to be non-zero!"


	

		Input.valuesList = [value1, value2, value3, value4, value5, value6, value7, value8]
		return Input.valuesList
		
	def GetDropDownValues(self):
		if self.comboBox_1.get() == 'Select Distribution': print "Box 1 has to have a selection"
		if self.comboBox_2.get() == 'Select Distribution': print "Box 2 has to have a selection"
		if self.comboBox_3.get() == 'Select Distribution': print "Box 3 has to have a selection"
		if self.comboBox_4.get() == 'Select Distribution': print "Box 4 has to have a selection"

		Input.distList = ["", self.comboBox_1.get(), self.comboBox_2.get(), "", "", self.comboBox_3.get(), self.comboBox_4.get(), ""]
		return Input.distList

	def CreateList(self):
		InputList = zip(Input.valuesList, Input.distList)
		return InputList
