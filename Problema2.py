#Considerando los terminos de la secuencia de Fibonacci cuyos valores no exceden los 4000000, encontrar la suma de los terminos pares.
#Utilizando cilo while se replica la secuencia de Fibonacci, deteniendose cuando la secuencia exceda los 4000000.
#Se utiliza if para verificar los valores pares y se realiza la suma.

a0 = 1
a1 = 1
F = 0
s = 0
while F < 4000000:
	F = a0 + a1
	a0 = a1
	a1 = F
	if F%2==0:
		s += F
print("Suma de pares es: " + str(s))

