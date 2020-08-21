def f1(*x):
	def f2():
		sum = 0
		for i in x:
			sum += i
		return sum
	return f2

f = f1(*[1,2,3])
print(f())

