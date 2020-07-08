#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import Thread,currentThread
from time import sleep,ctime

class CleanOutputSet(set):
	def __str__(self):
		return ', '.join(x for x in self)
	
loops = (randrange(2,5) for x in range(randrange(3,7)))

remaining = CleanOutputSet()

def loop(nsec):
	myname = currentThread().name
	remaining.add(name)
	print(f'[{ctime()}] Started {myname}')
	sleep(nsec)
	print(f'[(ctime)] Completed {myname} ({nsec} secs)')
	print(f' (remaining: {remainingi})')

def main():
	for pause in loops:
		Thread(target=loop, args=(pause,)).start()
	
@register
def _atexit():
	print(f'all DONE at: {ctime()}')



