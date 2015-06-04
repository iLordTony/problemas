a = int(raw_input()) + 1
contador = ''
for i in range(a):
	if (i % 2 == 0 and i != 0):
		contador = contador + '%s ' % i

print contador 