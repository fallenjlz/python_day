fish = 6

while True:
	total = fish
	flag = True
	for _ in range(5):
		if (total - 1) % 5 == 0:
			total = (total - 1) // 5 * 4
		else:
			flag = False
			break
	if flag:
		print(fish)
		break
	fish += 5

