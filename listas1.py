lista = [1,2,3,4,5,6,7,7,7,7,7,9,10,200,333]

for x in lista:
    if x % 2 == 1:
        lista.remove(x)

print(lista)

# Por qué quedan números impares en la lista?