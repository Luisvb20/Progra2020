#¿Cual es el 10001 numero primo?

# Creo un criba para los numero primos
def criba(numero):
	if numero in(0,1):
		return(False)
	for i in range(2, int(numero**(1/2))+1):
		if numero % i == 0:
			return(False)
	return(True)

#Correre un ciclo que contara los primos que salgan

i=0
j=0

while i < 10001:
	j=j+1
	if criba(j) == True:
		i = 1 + i

print(j)
