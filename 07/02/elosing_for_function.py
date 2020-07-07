#!/usr/bin/env python

def makeActions():
	acts = []
	for i in range(5):
		acts.append(lambda x: i**x)
	return acts

acts = makeActions()
print(acts[0])
print(acts[0](2))
print(acts[2](2))
print(acts[4](2))

def makeActions():
	acts1 = []
	for i in range(5):
		acts1.append(lambda x,i=i: i**x)
	return acts1

acts1 = makeActions()
print(acts1[0](2))
print(acts1[2](2))
print(acts1[4](2))
