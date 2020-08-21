#!/usr/bin/evn python

from math import sqrt

class Point(object):
	
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y

	def moveTo(self,x,y):
		self.x = x 
		self.y = y
	
	def moveBy(self,x,y):
		self.x += x
		self.y += y
	
	def distanceTo(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		dis = sqrt( dx ** 2 + dy ** 2)
		return dis
	
	def __str__(self):
		return '(%d,%d)' % (self.x, self.y)

def main():
	P1 = Point(1,2)
	P1.moveTo(-3,-4)
	P1.moveBy(1,6)
	print(P1)
	P = Point()
	print(P)
	d = P1.distanceTo(P)
	print(d)

if __name__ == '__main__':
	main()
	
