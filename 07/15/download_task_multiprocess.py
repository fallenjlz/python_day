from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
	print('%s begin to download, pid: %d' % (filename, getpid()))
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s download done use %d' % (filename, time_to_download))

def main():
	start = time()
	p1 = Process(target=download_task, args=('harry potter',))
	p1.start()
	p2 = Process(target=download_task, args=('war and peace',))
	p2.start()
	p1.join()
	p2.join()
	end = time()
	use_time = end - start
	print('download task use count: %d' % (use_time))

main()
