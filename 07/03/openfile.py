#!/usr/bin/env python

f = open('o.txt','r')
data = f.read()
print(data)
f.close()


f = open('o.txt', 'w')
f.write('reload')
f.close()

f = open('o.txt','r')
data = f.read()
print(data)
f.close()
