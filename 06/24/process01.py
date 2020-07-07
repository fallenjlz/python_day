#!/root/.pyenv/shims/python
from multiprocess import Process
import time

def drink_water():
	for i in range(4):
		print(f'bob drink {i} water')
		time.sleep(0.2)

		
def eat_breads():
	for i in range(4):
		print(f'bob eat {i} bread')
		time.sleep(0.2)

p1=Process(target=drink_water)
p2=Process(target=eat_breads)

p1.start()
p2.start()


