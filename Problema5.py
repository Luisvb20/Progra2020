#¿Cual es el numero positivo más pequeño que es divisible por todos los números del 1 al 20?

#Creando una funcion criba

def criba(numero):
	if numero in(0,1):
		return(False)
	for i in range(2, int(numero**(1/2))+1):
		if numero % i == 0:
			return(False)
	return(True)

#Creando funcion que encuentra al primo más grande un el intervalo

def maxprim(rango):
	while criba(rango) == False:
		rango = rango - 1
	return(rango)

mul=1
n=20

for i in range(maxprim(n)+1):
	t=i
	if criba(i) == True:
		while t < n:
			mul = mul * i
			t = t * i

print(mul)
		

