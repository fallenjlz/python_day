#!/root/.pyenv/shims/python
import re
m = re.match('foo','foo')
if m is not None:
		print(m.group())

m = re.match('foo','food on the table')
if m is not None:
		print(m.group())

m = re.match('foo','seafood')
if m is not None:
		print(m.group())
else:
		print('failed match')

m = re.search('foo','seafood')
if m is not None:
		print(m.group())

bt = 'bat|bet|bit'
m = re.match(bt,'bat')
if m is not None:
		print(m.group())


m = re.match(bt,'He bit me!')
if m is not None:
		print(m.group())
else:
		print('failed match')


m = re.search(bt,'He bit me!')
if m is not None:
		print(f'search {m.group()}')


anyend = '.end'
m = re.match(anyend,'bend')
if m is not None:
		print(m.group())

m = re.match(anyend,'end')
if m is not None:
		print(m.group())

m = re.match(anyend,'\nend')
if m is not None:
		print(m.group())
else:
		print('. cat\'t match \\n')

m = re.search(anyend,'The end')
if m is not None:
		print(m.group())


patt314 = '3.14'
pi_patt = '3\.14'

m = re.search(pi_patt,'3.14')
if m is not None:
		print(m.group())

m = re.search(patt314,'3014')
if m is not None:
		print(m.group())

m = re.search(patt314,'3.14')
if m is not None:
		print(m.group())

m = re.match('[cr][23][dp][o2]','c3po')
if m is not None: 
		print(m.group())

m = re.match('[cr][23][dp][o2]','c2do')
if m is not None: 
		print(m.group())

m = re.match('[cr][23][dp][o2]','r2d2')
if m is not None: 
		print(m.group())

patt='\w+@(\w+\.)?\w+\.com'
print(re.match(patt,'nobody@xxx.com').group())
print(re.match(patt,'nobody@www.xxx.com').group())


patt='\w+@(\w+\.)*\w+\.com'
print(re.match(patt,'nobody@www.yyy.zzz.xxx.com').group())

m = re.match('\w\w\w-\d\d\d','abc-123')
if m is not None:
	print(m.group())

m = re.match('\w\w\w-\d\d\d','abc-xyz')
if m is not None:
	print(m.group())

m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
if m is not None:
	print(m.group())
	print(m.group(1))
	print(m.group(2))

m = re.match('ab','ab')
print(m.group())
print(m.groups())

m = re.match('(ab)','ab')
print(m.group())
print(m.group(1))
print(m.groups())

m = re.match('(a)(b)', 'ab')
if m is not None:
	print(m.group())
	print(m.group(1))
	print(m.group(2))
	print(m.groups())

m = re.match('(a(b))', 'ab')
if m is not None:
	print(m.group())
	print(m.group(1))
	print(m.group(2))
	print(m.groups())


m = re.search('^The', 'The end.')
if m is not None:
	print(m.group())

m = re.search('^The', 'end. The')
if m is not None:
	print(m.group())

m = re.search(r'\bthe', 'bite the dog')
if m is not None:
	print(m.group())

m = re.search(r'\bthe', 'bitethe dog')
if m is not None:
	print(m.group())

m = re.search(r'\Bthe', 'bitethe dog')
if m is not None:
	print(m.group())

print(re.findall('car','car'))
print(re.findall('car','scary'))
print(re.findall('car','carry the barcardi to the car'))

s = 'This and that'
print(re.findall(r'(th\w+) and (th\w+)',s,re.I))

print(re.sub('X','Mr.Smith','attn: X\n\nDear X,\n'))
print(re.subn('X','Mr.Smith','attn: X\n\nDear X,\n'))

print(re.sub('[ae]','X','abcdef'))
print(re.subn('[ae]','X','abcdef'))

print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4})',r'\3/\1/\2','09/10/2007'))


print(re.split(':','str1:str2:str3'))

DATA = { 
	'Mountain View, CA 94040', 
	'Sunnyvale, CA',
	'Los Altos, 94023', 
	'Cupertino 95014',
	'Palo Alto CA',
}

for datum in DATA:
	print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))

print(re.findall(r'(?i)yes','yes? Yes. YES!!'))
print(re.findall(r'(?i)th\w+','The quickest way is through this tunnel.'))

print(re.findall(r'(?im)(^th[\w ]+)', """
... This line is the first,
... another line,
... that line, it's the best
... """))
