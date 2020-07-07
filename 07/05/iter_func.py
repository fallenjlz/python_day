#!/usr/bin/env python

res = []
for x in 'spam':
	res.append(ord(x))

print(res)

res = list(map(ord,'spam'))
print(res)
res = [ord(x) for x in 'spam']
print(res)

print([x ** 2 for x in range(10)])

print(tuple(filter(lambda x:x % 2 == 0,range(10))))

l = []
for i in range(10):
	if i % 2 == 0:
		l.append(i)

print(l)

print(tuple(map(lambda x: x**2, filter(lambda x:x % 2 == 0,range(10)))))

res = [ x + y for x in [0,1,2] for y in [100,200,300]]
print(res)

res = []
for x in [0,1,2]:
	for y in [100,200,300]:
		res.append(x + y)
print(res)

l = [ x + y for x in 'spam' for y in 'SPAM' ]
print(l)

l = [(x, y) for x in range(5) if x % 2 == 1 for y in range(5) if y % 2 == 0]
print(l)


M = [[1,2,3],
	[4,5,6],
	[7,8,9]]

N = [[2,2,2],
	[3,3,3],
	[4,4,4]]

print(M[1][2])

print([M[i][i] for i in range(len(M))])

print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print([[M[row][col] * N[row][col] for row in range(3)] for col in range(3)])
