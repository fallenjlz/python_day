from threading import Thread
from random import randint
from time import time,sleep

class DownloadTask(Thread):
	
	def __init__(self,filename):
		super().__init__()
		self.filename = filename

	def run(self):
		print('%s begin to download ' % (self.filename))
		time_to_download = randint(5,10)
		sleep(time_to_download)
		print('%s download done by %d s' % (self.filename, time_to_download))

def main():
	start = time()
	t1 = DownloadTask('harry potter')
	t1.start()
	t2 = DownloadTask('war and peace')
	t2.start()
	t1.join()
	t2.join()
	end = time()
	print('book download done by %.3f s' % ( end - start))

main()
