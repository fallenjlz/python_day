#!/usr/bin/env python

from random import randint

def generate_code(code_len=4):	
	code = ''
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) - 1
	for _ in range(code_len):
		random_pos = randint(0, last_pos)
		code += all_chars[random_pos]
	
	return code

print(generate_code())
print(generate_code(6))
print(generate_code(10))
		
