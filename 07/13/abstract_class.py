#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
	
	def __init__(self,nickname):
		self._nickname = nickname

	@abstractmethod
	def make_voice(self):
		pass


class Dog(Pet):

	def make_voice(self):
		return '%s 汪汪' % (self._nickname)

class Cat(Pet):

	def make_voice(self):
		return '%s 喵喵' % (self._nickname)

def main():
	for pet in ['bong','miao']:
		if pet == 'bong':
			print(Dog(pet).make_voice())
		else:
			print(Cat(pet).make_voice())

if __name__ == '__main__':
	main()
