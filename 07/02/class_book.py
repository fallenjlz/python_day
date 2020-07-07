#!/usr/bin/env python
class Book():
	def __init__(self, bname,author,year):
		self.__bname = bname
		self.author = author
		self.year = year

	@property
	def bname(self):
		return self.__bname
	
	@bname.setter
	def bname(self, bname):
		self.__bname = bname
	

	def __str__(self):
		return f'{self.bname} written by {self.author} in {str(self.year)}'

b1 = Book('town','tom',1995)
print(b1.bname)
b1.bname = 'harry'
print(b1)
