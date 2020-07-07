#!/usr/bin/env python

def kwonly(a,*b,c):
	print(a,b,c)

kwonly(1,2,c=3)
kwonly(3,5,c=6)

def kwonly(a,*,b,c):
	print(a,b,c)

kwonly(a=1,b=2,c=3)
kwonly(3,b=5,c=6)

def kwonly(a,*,b='spam',c='ham'):
	print(a,b,c)

kwonly(1,b=2)

def min1(*args):
	res = args[0]
	for i in args:
		if i < res:
			res = i
	return res

def min2(first,*args):
	res = first
	for i in args:
		if res < i:
			res = i
	return res

def min3(*args):
	l = list(args)
	res = l.sort()[0]
	return res

def minmax(func,*args):
	res = args[0]
	for i in args[1:]:
		if func(res,i):
			res = i
	return res

	
def lessthan(x,y): return x < y
def greaterthan(x,y): return x > y
l = list(range(10))
print(minmax(lessthan,*l))
print(minmax(greaterthan,*l))


def f(x,y):
	print(x+y)


L = [(1,2),(3,4)]

for x in L:
	f(*x)
	
