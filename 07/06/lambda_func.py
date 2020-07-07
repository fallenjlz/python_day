#!/usr/bin/env python
import sys
def func(x,y,z):return x+y+z

f = lambda x,y,z: x+y+z

print(func(2,3,4))
print(f(2,3,4))


L = [lambda x: x**2,
	lambda x: x**3,
	lambda x: x**4]

for f in L:
	print(f(2))

def f1(x): return x ** 2,
def f2(x): return x ** 3,
def f3(x): return x ** 4

L = [f1, f2, f3]

for f in L:
	print(f(2))


key = 'got'

x = {'already': (lambda: 2+2),
	'got': (lambda: 2*4),
	'one': (lambda: 2**6)}[key]()
print(x)

def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): return 2 ** 6

print({'already': f1,'got': f2,'one': f3}['one']())


lower = (lambda x,y: x if x < y else y)

print(lower('aa','bb'))

showall = lambda x: list(map(sys.stdout.write,x))
l = ['a\n','b\n','c\n']
print(showall(l))


def action(x):
	return lambda y: x + y

act1 = action(2)
print(act1(3))

action1 = (lambda x: (lambda y: x+y))
acts = action1(3)
print(acts(4))
print(((lambda x: (lambda y: x+y))(101))(4))

countes = [1,2,3,4]
updated = []
for x in countes:
	updated.append(x+10)
print(updated)

def inc(x):
	return x * 10

updated = list(map(inc, countes))
print(updated)

print(list(map((lambda x: x/10), countes)))

def mymap(f,l):
	res = []
	for x in l:
		res.append(f(x))
	return res
print(list(mymap((lambda x: x/20), countes)))


print(mymap(inc,countes))

print(pow(3,4))

print(list(map(pow,[1,2,3],[2,3,4])))
print(list(map((lambda x: x/10), countes)))

print(list(range(-5,5)))

print(list(filter(lambda x: x>0, range(-5,5))))
