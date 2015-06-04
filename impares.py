a = raw_input().split(' ')
for i in a:
	if (int(i) % 2 != 0):
		print a.index(i) + 1
		break