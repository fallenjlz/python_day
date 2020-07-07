#!/usr/bin/env python
def s(x):
	print(x)

def times(x,y):
	return x * y

s(times(2,4))
s(times('Ni',4))


def intersect(seq1, seq2):
	res = []
	for i in seq1:
		if i in seq2:
			res.append(i)
	return res

l1 = list(range(0,10))
l2 = list(range(5, 12))
s(intersect(l1,l2))


#Globe scope
x = 99 
def func(y):
	z = x + y
	return z
s(func(1))

X = 88

def func():
	X = 99
func()
print(X)

def func():
	global X 
	X = 99
func()
print(X)

y,z = 1,2

def all_global():
	global x 
	x = y + z
s(x)
