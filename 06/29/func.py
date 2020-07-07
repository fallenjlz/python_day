#!/usr/bin/env python

def f(a, *b, c=6, **d):
	print(a, b, c, d)

f(1,2,3,x=4,y=6)

l = [2,3,4]
d = {'y':'9'}

f('x',*l,**d)


def mysum(L):
	if not L:
		return 0
	else:
		return L[0] + mysum(L[1:])

s = mysum(l)
print(s)
	
