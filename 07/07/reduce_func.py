#!/usr/bin/env python

from functools import reduce

print(reduce(lambda x,y: x+y,[1,2,3,4]))

def f(x,y):
	return x ** y

print(reduce(f,[2,3,4,5]))

