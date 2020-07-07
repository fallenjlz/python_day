#!/usr/bin/env python

def f(*args): print(args)

f(1,2)

def f(**args): print(args)
f(a=1,b=2)

def f(a,*args,**kwargs): print(a,args,kwargs)
f(1,2,3,x=1,y=2)

#解包
def f(a,b,c,d):
	print(a,b,c,d)

l = [1,2,3,4]
d = {'a':'A','b':'B','c':'C','d':'D'}
f(*l)
f(**d)

f(*(2,3),**{'c':4,'d':5})
f(1,*(2,3),**{'d':5})
f(1,*(2,),**{'c':4,'d':5})
f(1,*(2,),c=4,**{'d':5})
