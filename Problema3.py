#¿Cual es el factor primo más grande del numero 600851475143?
#Probando factor por factor empezando desde el más pequeño utilizando ciclo while
#La primera condición es para asegurar que el ciclo pare, ningun factor será más grande que el numero a evaluar
#El segundo while comparará si es factor o no, si es factor entonces la división será entera y la reemplazare por una nueva n.
#Finalmente correré un paso f hasta entonctrar otro valor menor al numero a evaluar.
n=600851475143
f=2
while f < n:
	while n%f == 0:
		n = n / f
	f=f+1
print (f)
	
