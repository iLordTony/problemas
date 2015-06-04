contador = 0
impar = 0
cinco = 0
siete = 0
for i in range(0, 101):
	print "El numero es: ", i
	if (i % 2 == 0):
		contador+=1
	else:
		impar+=1
	if(i % 5 == 0):
		cinco+=1
	if ("7" in str(i)):
		siete+=1

print "El numero de pares es: ", contador
print "El numero de impares es: ", impar
print "El numero de cincos es: ", cinco
print "El numero de 7 es: ", siete