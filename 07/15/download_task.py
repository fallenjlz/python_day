from random import randint
from time import time,sleep

def download_task(filename):
	print('%s Begin to download ...' % (filename))
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s download done %d' % (filename,time_to_download))

def main():
	start = time()
	download_task('harry potter')
	download_task('war and pearce')
	end = time()
	use_time = end - start
	print(' use time conunt: %d' % (use_time))

main()
