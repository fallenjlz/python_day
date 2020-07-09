#!/usr/bin/env python

def is_leap_year(year):
	
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,day):
	
	days = 0

	if is_leap_year:
		days_of_month=[31,29,31,30,31,30,31,31,30,31,30,31]
	else:
		days_of_month=[31,28,31,30,31,30,31,31,30,31,30,31]

	for i in range(month - 1):
		days += days_of_month[i]
	
	total = days + day

	return 'The %d day' % total

if __name__ == '__main__':
	print(which_day(2007,8,23))
	print(which_day(2020,7,10))
	print(which_day(2020,7,9))

		
