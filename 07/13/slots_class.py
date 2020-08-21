#!/usr/bin/env python

class Person(object):
	__slots__ = ['_name','_age','_gender']

	def __init__(self,name,age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name
	
	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,age):
		self._age = age

	def __str__(self):
		if self._age < 16:
			return '%s is playing chess' % (self._name)
		else:
			return '%s is playing puke' % (self._name)

if __name__ == '__main__':
	p = Person('Bob',18)
	p.age = 16
	p._gender = 'male'
	print(p)

			
