#Encontrar la suma de todos los multiplos de 3 o 5 de bajo de 1000
#Recorremos los numeros de 3 a 1000 mediante un ciclo for
#Se revisa la condicion mediante if

sum=0
for x in range(3,1001):
    if x%3 == 0 or x%5 == 0:
        sum=sum+x

print(sum)
