#!/usr/bin/env python

import os
from time import sleep


def main():
	content = '北京欢迎你为你开天辟地......'
	while True:
		os.system('clear')
		print(content)
		sleep(0.2)
		content = content[1:] + content[0]

if __name__ == '__main__':
	main()
	
