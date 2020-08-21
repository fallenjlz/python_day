from threading import Thread
from random import randint
from time import time,sleep

def download_task(filename):
	print('%s begin to download' % (filename))
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s download done %d ' % (filename, time_to_download))

def main():
	start = time()
	t1 = Thread(target=download_task,args=('harry potter',))
	t1.start()
	t2 = Thread(target=download_task,args=('war and peace',))
	t2.start()
	t1.join()
	t2.join()
	end = time()
	use_time = end - start
	print('download task done %f ' % (use_time))

main()
