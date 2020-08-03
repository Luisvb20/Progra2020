# Encontrar la suma de todos los primos menores que dos millones

#Creo una funcion criba para separar numeros primos
def criba(numero):
	if numero in(0,1):
		return(False)
	for i in range(2, int(numero**(1/2))+1):
		if numero % i == 0:
			return(False)
	return(True)

#sumo los numeros primos en el rango deseado

suma=0

for i in range(2,2000000):
	if criba(i) == True:
		suma = suma + i
	

print(suma)
