#!/usr/bin/env python

def test(x):
	y = x 
	def nested(z):
		nonlocal y
		print(z, y)
		y += 1
	return nested 

f = test(2)
f(3)
		
	
