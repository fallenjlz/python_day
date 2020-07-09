#!/usr/bin/env python

def max2(x):
	m1, m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
	for index in range(2,len(x)):
		if x[index] > m1:
			m2 = m1
			m1 = x[index]
		elif x[index] > m2:
			m2 = x[index]
	return m1,m2

l = [100,2000,40000,23242342,2903402,3243,234,1342,5352,12]
print(max2(l))
