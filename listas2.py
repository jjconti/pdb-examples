def guardar(numero, lista=[]):
    lista.append(numero)
    return lista

mi_lista = guardar(1)
print(mi_lista)

otra_lista = guardar(2)
print(otra_lista)

# Por qué no funciona como se espera?