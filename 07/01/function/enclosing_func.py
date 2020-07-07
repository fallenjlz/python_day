#!/usr/bin/env python
X = 99

def f1():
	X = 88
	def f2():
		print(X)
	f2()

f1()

def f1():
	X = 88
	def f2():
		print(X)
	return f2

action = f1()
action()

def maker(N):
	def action(X):
		return X ** N
	return action

f = maker(3)
print(f(2))
print(f(3))

#避免嵌套
def f1():
	x = 88
	f2(x)

def f2(x):
	print(x)

f1()
