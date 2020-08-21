#!/usr/bin/env python


from time import sleep, time, localtime
import os
class Clock(object):
	
	def __init__(self,seconds,minutes,hours):
		self._seconds = seconds
		self._minutes = minutes
		self._hours = hours

	@classmethod
	def now(cls):
		ctime = localtime(time())
		return cls(ctime.tm_sec,ctime.tm_min,ctime.tm_hour)

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
	def __str__(self):
		os.system('clear')
		return '%02d:%02d:%02d' % (self._hours, self._minutes, self._seconds)

if __name__ == '__main__':
	clock = Clock.now()
	while True:
		print(clock)
		sleep(1)
		clock.run()



	
