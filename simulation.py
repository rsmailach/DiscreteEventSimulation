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

class Model:
	def __init__(self):
		self.ArrivalRate = None				# lambda
		self.ArrivalDist = None
		self.ServiceRate = None				# mu
		self.ServiceDist = None
		#TurnonTime = self.inputList[3][0]
		#JobThreshold = self.inputList[4][0]	# k
		#TurnoffRate = self.inputList[5][0]	# alpha
		#upStateRate = self.inputList[6][0]	# gamma
		self.MaxSimTime = 0.0	# simulation length

	def GetList(self):
		print "GetList from Model has been run"
		
		# grab all input values
		var = main.MyWindow
		print "1111"
		self.inputList = var.GetList(parent)
		print "222"
		

		self.NumMachines = self.inputList[0][0]
		self.ArrivalRate = self.inputList[1][0]	# lambda
		self.ArrivalDist = self.inputList[1][1]
		self.ServiceRate = self.inputList[2][0]	# mu
		self.ServiceDist = self.inputList[2][1]
		self.TurnonTime = self.inputList[3][0]
		self.JobThreshold = self.inputList[4][0]	# k
		self.TurnoffRate = self.inputList[5][0]	# alpha
		self.upStateRate = self.inputList[6][0]	# gamma
		self.MaxSimTime = self.inputList[7][0]	# simulation length

		ArrivalDistributions =  {
			'Exponential': Rnd.expovariate(self.ArrivalRate),
			'Normal': Rnd.normalvariate(self.ArrivalRate)
			#'Custom':
		}

		ServiceDistributions =  {
			'Exponential': Rnd.expovariate(self.ServiceRate),
			'Normal': Rnd.normalvariate(self.ServiceRate)
			#'Custom':
		}
		print "end of GetList"

	def Run(self):
		print "Run from Model has been run"
		self.GetList()
		initialize()
		print "Initialize has been run"
		for I in range(NumMachines):
			M = MachineClass()
			activate(M,M.Run())	
		A = ArrivalClass()
		activate(A, A.Run())
		simulate(until = MaxSimTime)
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
		return Model.ServiceDistributions[ServiceDist]


	def Run(self):
		while 1:
			# sleep until this machine awakened
			yield passivate, self
			MachineClass.Idle.remove(self)
			MachineClass.Busy.append(self)

			# take next job in queue
			while MachineClass.Queue != []:
				Job = MachineClass.Queue.pop(0)		# get job
				yield hold,self, SetServiceDist(ServiceDist) # service job
				MachineClass.JobServiceTime += now() - Job.ArrivalTime # total wait time of all completed jobs, including queuing and service times

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
		return Model.ArrivalDistributions[ArrivalDist]


	def Run(self):
		while 1:
			# wait for arrival of next job
			yield hold, self, SetArrivalDist(ArrivalDist)

			Job = JobClass()
			MachineClass.Queue.append(Job)

			# check if any machines are idle and ready for work
			if MachineClass.Idle != []:
				reactivate(MachineClass.Idle[0])


class Globals:
	Rnd = Random(12345)	

