a = int(raw_input())
b = raw_input().split(' ')
contador = 0
impar = 0
for i in range(a):
	if (int(b[i]) % 2 == 0):
		contador+=1
	else:
		impar+=1

print contador, impar