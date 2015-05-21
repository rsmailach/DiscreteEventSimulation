#----------------------------------------------------------------------#
# simulate.py
#  
# This class is used to simulate the specified model.
# 
# Rachel Mailach
#----------------------------------------------------------------------#

from SimPy.Simulation import *
from random import Random,expovariate,uniform,normalvariate # https://docs.python.org/2/library/random.html
#from Tkinter import *
import gui
import main

class Globals:
	Rnd = Random(12345)	

class Model(gui.Input, object):
	def __init__(self):
		self.ArrivalRate = None				# lambda
		Model.ArrivalDist = None
		self.ServiceRate = None				# mu
		Model.ServiceDist = None
		#TurnonTime = self.inputList[3][0]
		#JobThreshold = self.inputList[4][0]	# k
		#TurnoffRate = self.inputList[5][0]	# alpha
		#upStateRate = self.inputList[6][0]	# gamma
		self.MaxSimTime = 0.0	# simulation length

	def GetList(self):	
		# grab all input values
		self.inputList = super(Model, self).CreateList()		

		self.NumMachines = int(self.inputList[0][0])
		self.ArrivalRate = self.inputList[1][0]	# lambda
		Model.ArrivalDist = self.inputList[1][1]
		self.ServiceRate = self.inputList[2][0]	# mu
		Model.ServiceDist = self.inputList[2][1]
		self.TurnonTime = self.inputList[3][0]
		self.JobThreshold = self.inputList[4][0]	# k
		self.TurnoffRate = self.inputList[5][0]	# alpha
		self.upStateRate = self.inputList[6][0]	# gamma
		self.MaxSimTime = self.inputList[7][0]	# simulation length

		Model.ArrivalDistributions =  {
			'Exponential': Globals.Rnd.expovariate(self.ArrivalRate),
			#'Normal': Globals.Rnd.normalvariate(self.ArrivalRate)
			#'Custom':
		}

		Model.ServiceDistributions =  {
			'Exponential': Globals.Rnd.expovariate(self.ServiceRate),
			#'Normal': Globals.Rnd.normalvariate(self.ServiceRate)
			#'Custom':
		}

	def Run(self):
		self.GetList()
		initialize()
		
		for I in range(self.NumMachines):
			M = MachineClass()
			activate(M,M.Run())	
		A = ArrivalClass()
		activate(A, A.Run())
		simulate(until = self.MaxSimTime)
		print "Done simulation!"

class MachineClass(Process):
	Busy = []	# busy machines
	Idle = []	# idle machines
	Queue = []	# queued for the machines
	IdlingTime = 0.0
	JobServiceTime = 0.0

	def __init__(self):
		Process.__init__(self)
		MachineClass.Idle.append(self)	# starts idle
	
		
	# dictionary of service distributions
	def SetServiceDist(self):
		return Model.ServiceDistributions[Model.ServiceDist]


	def Run(self):
		while 1:
			# sleep until this machine awakened
			yield passivate, self
			MachineClass.Idle.remove(self)
			MachineClass.Busy.append(self)

			# take next job in queue
			while MachineClass.Queue != []:
				Job = MachineClass.Queue.pop(0)		# get job
				yield hold,self, self.SetServiceDist() #ServiceDist) # service job

		MachineClass.Busy.remove(self)
		MachineClass.Idle.append(self)



class JobClass:			
	def __init__(self):
		self.ArrivalTime = now()


class ArrivalClass(Process):
	def __init__(self):
		Process.__init__(self)
		
	# dictionary of arrival distributions
	def SetArrivalDist(self):
		return Model.ArrivalDistributions[Model.ArrivalDist]


	def Run(self):
		while 1:
			# wait for arrival of next job			
			yield hold, self, self.SetArrivalDist() #Model.ArrivalDist)

			Job = JobClass()
			MachineClass.Queue.append(Job)

			# check if any machines are idle and ready for work
			if MachineClass.Idle != []:
				reactivate(MachineClass.Idle[0])
