def bubble_sort(items, comp=lambda x,y: x > y):
	
	items = items[:]
	for i in range(len(items) - 1):
		flag = False
		for j in range(len(items) - 1 -i ):
			if comp(items[j],items[j+1]):
				items[j],items[j+1] = items[j+1], items[j]
				flag = True
		flag = False
		for j in range(len(items) - 2 -i, 0, -1):
			if comp(items[j], items[j-1]):
				items[j],items[j-1] = items[j-1], items[j]
				flag = True

		if not flag:
			break
	return items

l = [9,3,5,3,78,2,1,5]
print(bubble_sort(l))


