#!/usr/bin/env python

def fac(x):
	if x < 2: return 1
	return x * fac(x-1)

print(fac(10))
print(fac(20))

def factorial(num):
	answer=1
	if num ==  1:
		answer = 1
	else:
		for x in range(2,num+1):
			answer*=x
	return answer

print(factorial(10))
print(factorial(20))
