#cual es la suma de los digitos de 2^1000
#se puede pasar un entero a una cadena.
n=2**1000
suma = 0
for i in str(n):
	suma += int(i)
print(suma)

#otra manera es
'''
digito = [int(i) for i in str(2**100)]
print(sum(digito))
'''
