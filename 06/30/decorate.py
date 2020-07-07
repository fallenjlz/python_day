#!/usr/bin/env python

def decorate(func):
	def wrapper():
		print('in decorate')
		func()
	return wrapper


@decorate
def test():
	print('hello')

test()


	
