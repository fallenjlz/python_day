#!/usr/bin/env python

from math import sqrt
import os

class Triangle(object):
	
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	@staticmethod
	def is_valid(a, b, c):
		return a + b > c and a + c > b and b + c > a

	def primeter(self):
		return self.a + self.b + self.c

	def area(self):
		half = self.primeter() / 2
		return sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))
	
def main():
	a = int(input(' input length a: '))
	b = int(input(' input length b: '))
	c = int(input(' input length c: '))
	if Triangle.is_valid(a,b,c):
		t = Triangle(a,b,c)
		print(t.primeter())
		print(t.area())
	else:
		os.system('clear')
		print('%d %d %d 无法组成三角形' % (a, b, c))


if __name__ == '__main__':
	main()	
	
