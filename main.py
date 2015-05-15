#----------------------------------------------------------------------------------#
# main.py
#  
# This class is used as a graphical user interface for a larger application.
# 
# Rachel Mailach
#----------------------------------------------------------------------------------#

from Tkinter import *
import ttk


class MyWindow(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)	# Because GUIs are hierarchical, it is a good idea to keep track of parent widgets
		self.parent = parent		# reference to parent
		self.initialize()

	def initialize(self):			# initialize widgets in this method
		self.grid()					# display widgets as grid

		# create widgets, parent = self because our window is the parent of these widgets
		self.numServers = Label(self, text = "number of servers")	# number of servers
		self.arrivalRate = Label(self, text = u'\u03bb')			# lambda
		self.serviceRate = Label(self, text = u'\u03bc')			# mu
		self.turnonTime = Label(self, text = "turn-on time")		# turn-on time
		self.jobThreshold = Label(self, text = "k")					# k
		self.turnoffRate = Label(self, text = u'\u03b1')			# alpha
		self.upStateRate = Label(self, text = u'\u0263')			# gamma
		
		
		self.entry_1 = Entry(self)
		self.entry_2 = Entry(self)
		self.entry_3 = Entry(self)
		self.entry_4 = Entry(self)
		self.entry_5 = Entry(self)
		self.entry_6 = Entry(self)
		self.entry_7 = Entry(self)

		self.button = Button(self, text = "SIMULATE", command = self.OnButtonClick)

		# Menu
		#dropDown = Menu(self)
		#self.config(menu = dropDown)
		#subMenu = Menu(dropDown)
		#dropDown.add_cascade(label = "Distribution", menu = subMenu)
		#subMenu.add_command(label = "Exponential", command = self.DropDown)
		#subMenu.add_separator()
		#subMenu.add_command(label = "Custom", command = self.DropDown)

		self.distributions = ('Select Distribution', ttk.Separator(self, orient = HORIZONTAL), 'Exponential', 'Normal', 'Custom')
		self.combo = ttk.Labelframe(self, text = 'Distributions')
		self.comboBox_1 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_1.current(0) # set selection
		self.comboBox_1.bind('<<ComboboxSelected>>', self.DropDown)
		self.comboBox_2 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_2.current(0) # set selection
		self.comboBox_2.bind('<<ComboboxSelected>>', self.DropDown)
		self.comboBox_3 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_3.current(0) # set selection
		self.comboBox_3.bind('<<ComboboxSelected>>', self.DropDown)
		self.comboBox_4 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_4.current(0) # set selection
		self.comboBox_4.bind('<<ComboboxSelected>>', self.DropDown)
		self.comboBox_5 = ttk.Combobox(self, values = self.distributions, state = 'readonly')
		self.comboBox_5.current(0) # set selection
		self.comboBox_5.bind('<<ComboboxSelected>>', self.DropDown)

		# send to layout manager 
		self.numServers.grid(row = 0, column = 0)
		self.arrivalRate.grid(row = 1, column = 0)
		self.serviceRate.grid(row = 2, column = 0)
		self.turnonTime.grid(row = 3, column = 0)
		self.jobThreshold.grid(row = 0, column = 5)
		self.turnoffRate.grid(row = 1, column = 5)
		self.upStateRate.grid(row = 2, column = 5)

		self.entry_1.grid(row = 0, column = 1)
		self.entry_2.grid(row = 1, column = 1)
		self.entry_3.grid(row = 2, column = 1)
		self.entry_4.grid(row = 3, column = 1)
		self.entry_5.grid(row = 0, column = 6)
		self.entry_6.grid(row = 1, column = 6)
		self.entry_7.grid(row = 2, column = 6)

		self.button.grid(row = 8, columnspan = 7)
	
		self.comboBox_1.grid(row = 1, column = 3)
		self.comboBox_2.grid(row = 2, column = 3)
		self.comboBox_3.grid(row = 3, column = 3)
		self.comboBox_4.grid(row = 0, column = 7)
		self.comboBox_5.grid(row = 1, column = 7)


	def OnButtonClick(self):
		# DO SOMETHING!#
		#make num servers an int
		print "You clicked the button!"

	def DropDown(self, event):
		#self.value_of_combo = self.box.get()
		#print(self.value_of_combo)
		widget = event.widget		# get widget
		text = widget.get()			# get widget text
		value = widget.cget('values')	# get values
		print text

def main():
	window = MyWindow(None)						# instantiate the class with no parent (None)
	window.title('Discrete Event Simulation')	# title the window	
	#window.geometry("500x600")					# set window size
	window.mainloop()							# loop indefinitely, wait for events


if __name__ == '__main__': main()

