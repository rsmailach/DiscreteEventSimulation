#----------------------------------------------------------------------#
# simulation.py
#  
# This class is used to simulate the specified model.
# 
# Rachel Mailach
#----------------------------------------------------------------------#

from SimPy.Simulation import *
from random import Random,expovariate,uniform,normalvariate # https://docs.python.org/2/library/random.html
#from Tkinter import *
import guiInput
import main
import math


class Globals:
	def __init__(self, parent):
		self.parent = parent
		Globals.Rnd = Random(12345)
		Globals.NumMachines = 0
		Globals.ArrivalRate = 0.0
		Globals.ArrivalDist = ""
		Globals.ServiceRate = 0.0
		Globals.ServiceDist = ""
		Globals.TurnonTime = 0.0
		Globals.JobThreshold = 0.0
		Globals.TurnoffRate = 0.0
		Globals.MaxSimTime = 0.0
		Globals.ArrivalDistributions = {}
		Globals.ServiceDistributions = {}

	def GetList(self):	
		# grab all input values
	#	self.inputList = super(Model, self).CreateList()
		inputInstance = guiInput.Input(self.parent)
		inputList = inputInstance.CreateList()		

		Globals.NumMachines = int(inputList[0][0])
		Globals.ArrivalRate = inputList[1][0]	# lambda
		Globals.ArrivalDist = inputList[1][1]
		Globals.ServiceRate = inputList[2][0]	# mu
		Globals.ServiceDist = inputList[2][1]
		Globals.TurnonTime = inputList[3][0]
		Globals.JobThreshold = inputList[4][0]	# k
		Globals.TurnoffRate = inputList[5][0]	# alpha
		Globals.upStateRate = inputList[6][0]	# gamma
		Globals.MaxSimTime = inputList[7][0]	# simulation length

		Globals.ArrivalDistributions =  {
			'Exponential': Globals.Rnd.expovariate(Globals.ArrivalRate),
			#'Normal': Globals.Rnd.normalvariate(self.ArrivalRate)
			#'Custom':
		}

		Globals.ServiceDistributions =  {
			'Exponential': Globals.Rnd.expovariate(Globals.ServiceRate),
			#'Normal': Globals.Rnd.normalvariate(self.ServiceRate)
			#'Custom':
		}
		
		Globals.rho = Globals.ArrivalRate/Globals.ServiceRate
		Globals.Utilization = Globals.ArrivalRate/(Globals.ServiceRate*Globals.NumMachines)

# for M/M/c
def LimitingProbability():	
	sum1 = 0
	for iterator in range (1, Globals.NumMachines): # from 1 to NumServers - 1
		sum1 += (1.0/math.factorial(iterator)) *\
				pow((Globals.ArrivalRate/Globals.ServiceRate),iterator)

	rho = Globals.ArrivalRate / (Globals.NumMachines * Globals.ServiceRate)
	eqn = 	(1.0/math.factorial(Globals.NumMachines)) *\
			pow((Globals.ArrivalRate/Globals.ServiceRate), Globals.NumMachines) *\
			(1.0 / (1.0 - rho))

	pi_0 = pow((1.0 + sum1 + eqn), (-1))
	return pi_0

# for M/M/c
def ResponseTime():
	expectedRT = (1/Globals.ServiceRate)*\
			+ ((pow((Globals.rho), Globals.NumMachines)*Globals.ServiceRate)/((math.factorial(Globals.NumMachines - 1)) * pow((Globals.NumMachines*Globals.ServiceRate - Globals.ArrivalRate), 2)))*LimitingProbability()
	return expectedRT

def TimeQueued():
	timeQueued = ((pow(Globals.rho, Globals.NumMachines)*Globals.ServiceRate)/((math.factorial(Globals.NumMachines - 1)) * pow((Globals.NumMachines*Globals.ServiceRate - Globals.ArrivalRate), 2)))*LimitingProbability()
	return timeQueued

# for M/M/c---------------------???? incorrect?
def NumJobs():
	numJobs = Globals.ArrivalRate * ResponseTime()
	return numJobs

# for M/M/c
def NumJobsQueued():
	numJobsQueued = ((pow((Globals.rho), Globals.NumMachines)*Globals.ArrivalRate*Globals.ServiceRate)/(math.factorial(Globals.NumMachines - 1)*pow(Globals.NumMachines*Globals.ServiceRate - Globals.ArrivalRate, 2))) * LimitingProbability()
	return numJobsQueued

def CreateOutputList():
	OutputList = [Globals.Utilization, LimitingProbability(), ResponseTime(), TimeQueued(), NumJobs(), NumJobsQueued()]

	# formats floats to 4 decimal places
	#OutputList = [ '%.4f' % elem for elem in OutputList ]
	return OutputList

def Run(self):
	globalsInstance = Globals(self)
	globalsInstance.GetList()
	initialize()
		
	for I in range(Globals.NumMachines):
		M = MachineClass()
		activate(M,M.Run())	
	A = ArrivalClass()
	activate(A, A.Run())
	simulate(until = Globals.MaxSimTime)
	CreateOutputList()
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
		return Globals.ServiceDistributions[Globals.ServiceDist]


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
		return Globals.ArrivalDistributions[Globals.ArrivalDist]


	def Run(self):
		while 1:
			# wait for arrival of next job			
			yield hold, self, self.SetArrivalDist() #Model.ArrivalDist)

			Job = JobClass()
			MachineClass.Queue.append(Job)

			# check if any machines are idle and ready for work
			if MachineClass.Idle != []:
				reactivate(MachineClass.Idle[0])
