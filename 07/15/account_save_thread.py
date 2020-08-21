from threading import Thread, Lock
from time import sleep

class Account(object):
	
	def __init__(self):
		self._balance = 0
		self._lock = Lock()

	def deposite(self,money):
		self._lock.acquire()
		try:
			new_balance = self._balance + money
			sleep(0.1)
			self._balance = new_balance
		finally:
			self._lock.release()
	
	@property
	def balance(self):
		return self._balance
	
class Add_money(Thread):
	
	def __init__(self, account, money):
		super().__init__()
		self._account = account
		self._money = money
	
	def run(self):
		self._account.deposite(self._money)

def main():
	
	account = Account()
	threads = []
	for _ in range(100):
		t = Add_money(account,1)
		threads.append(t)
		t.start()
	
	for t in threads:
		t.join()

	print(' account balance: %d' % ( account.balance ))

main()



