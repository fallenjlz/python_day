#!/usr/bin/env python

#has_dot 是否需要后缀名加点
#filename 传入的文件名

def get_suffix(filename,has_dot=False):
	pos = filename.rfind('.')
	if 0 < pos < len(filename) - 1:
		index = pos if has_dot else pos + 1
		return filename[index:]
	else:
		return '' 

print(get_suffix('test.py.sh'))
print(get_suffix('test.py.sh', True))


