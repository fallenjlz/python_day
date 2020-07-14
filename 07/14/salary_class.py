#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Employer(object, metaclass=ABCMeta):
	
	def __init__(self,name):
		self.name = name

	@abstractmethod
	def get_salary(self):
		pass

class Manager(Employer):
	
	def get_salary(self):
		return '15000'

class Programmer(Employer):
	
	def __init__(self,name,work_hours=0):
		super().__init__(name)
		self._work_hours = work_hours

	@property
	def work_hours(self):
		return self._work_hours 

	@work_hours.setter
	def work_hours(self,hours):
		self._work_hours = hours if hours > 0 else 0
	
	def get_salary(self):
		salary = 150 * self._work_hours
		return salary

class Saler(Employer):
	
	def __init__(self,name,sales=0):
		super().__init__(name)
		self._sales = sales

	@property
	def sales(self):
		return self._sales 
	
	@sales.setter
	def sales(self,n_sale):
		self._sales = n_sale if n_sale > 0 else 0

	def get_salary(self):
		salary = 7000 + 0.05 * self._sales
		return salary

def main():
	emps = [
		Manager('bob'), Manager('kate'),
		Programmer('kali'), Programmer('jerry',200),
		Saler('mark'), Saler('lina',200000)
	]

	for emp in emps:
		if isinstance(emp, Programmer):
			work_hours = int(input('%s input working hours: ' % emp.name))
			emp.work_hours = work_hours
			print(emp.get_salary())
		elif isinstance(emp,Saler):
			sales = int(input('%s input sales number: ' % emp.name))
			emp.sales = sales
			print(emp.get_salary())
		else:		
			print(emp.get_salary())

main()
		
	
