#!/usr/bin/env python

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as open

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com./dp/'
ISBNS = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
	page = uopen('%s

