from threading import Thread
from mercurysms import twilio

class Worker:

	def __init__(self):
		self.worker = Thread()
		self.err_nums = []
		self.cost = 0.0
		self.done = False

	def start_process(self, message, numbers):
		self.worker = Thread(target=self.__process, args=(message, numbers))
		self.worker.start()

	def reset(self):
		self.worker = Thread()
		self.err_nums = []
		self.cost = 0.0
		self.done = False

	def __process(self, message, numbers):
		self.err_nums, self.cost = twilio.mass_sms(message, numbers)
		self.done = True
