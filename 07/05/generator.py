#!/usr/bin/env python

import math

def gensquares(N):
	for i in range(N):
		yield i ** N

x = gensquares(4)
print(x)

while True:
	try:
		print(next(x))
	except:
		print('run out')
		break


g = ( x ** 2 for x in range(2,6))

for x in g:
	print(x, end=':')

while True:
	try:
		print(next(g))
	except:
		break

def gen():
	for x in range(10):
		y = yield x
		print(y)

g = gen()
print(next(g))
print(g.send('hello'))

for num in ( x ** 2 for x in range(4)):
	print(f'{num} {num/2.0}')


print(sum(x for x in range(100)))
print(sorted(x ** 2 for x in range(100)))

print(list(map(math.sqrt, ( x ** 2 for x in range(4)))))


