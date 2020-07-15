import time

f = open('jupyter.conf','r',encoding='utf-8')
print(f.read())
f.close()

try:
	f = open('default.conf','r',encoding='utf-8')
except FileNotFoundError:
	print('Can\'t find this file')
finally:
	if f:
		f.close()



f = open('jupyter.conf','r',encoding='utf-8')
for row in f.readlines():
	print(row)
f.close()

f = open('jupyter.conf','r',encoding='utf-8')

time.sleep(0.5)
f.readline()

f.close()

