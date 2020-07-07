#!/usr/bin/env python

def test(x):
	def intest(b):
		nonlocal x
		x += b
		return x
	return intest

a = test(2)
print(a(3))
print(a(8))	
