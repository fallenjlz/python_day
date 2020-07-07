#!/usr/bin/env python

def mysum(L):
	if not L:
		return L[0]
	else:
		return L[0] + mysum(L[1:])

def mysum(L):
	if len(L) == 1:
		return L[0]
	else:
		return L[0] + mysum(L[1:])

L = [1,2,3,4,5]
sum = 0

while L:
	sum += L[0]
	L = L[1:]

print(sum)

def sumtree(L):
	sum = 0
	for i in L:
		if not isinstance(i,list):
			sum += i
		else:
			sum += sumtree(i)
	return sum

l = [1,[2,3,[4,5]],[6,[7,[8,9],10]],]
print(sumtree(l))

