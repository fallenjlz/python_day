#!/usr/bin/env

for x in range(0,20):
	for y in range(0,33):
		z = 100 - x - y
		if x * 5 + y * 3 + z / 3 == 100:
			print(x, y, z)
