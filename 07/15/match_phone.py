import re

def main():
	sentence = '''
	    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
		    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
			    '''
				 
	m = re.findall(r'(?<=\D)1[34578]\d{9}(?=\D)', sentence)
	print(m)

	p = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
	for P in p.finditer(sentence):
		print(P.group())

main()
