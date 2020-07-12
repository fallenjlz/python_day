#!/usr/bin/env python


from time import sleep
import os
class Clock(object):
	
	def __init__(self,seconds,minutes,hours):
		self._seconds = seconds
		self._minutes = minutes
		self._hours = hours

	def run(self):
		self._seconds += 1
		if self._seconds == 60:
			self._seconds = 0
			self._minutes += 1
			if self._minutes == 60:
				self._minutes = 0
				self._hours += 1
				if self._hours == 24:
					self._hours = 0
	def show(self):
		os.system('clear')
		print('%02d:%02d:%02d' % (self._hours, self._minutes, self._seconds))

if __name__ == '__main__':
	clock = Clock(0,0,0)
	while True:
		clock.run()
		sleep(1)
		clock.show()



	
