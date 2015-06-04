def fib(n):
 	a,b = 1,1
 	contador = ''
 	for i in range(n-1):
 		a,b = b,a+b
 		if a > n:
  			break
  		contador = contador + '%s ' % a
 	return contador
k = int(raw_input())
print fib(k)