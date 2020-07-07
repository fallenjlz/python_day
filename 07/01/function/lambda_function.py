#!/usr/bin/env python

def func():
	x = 4
	action = (lambda n : x**n)
	print(id(action))
	return action

f = func()
print(id(f))
print(f(2))

