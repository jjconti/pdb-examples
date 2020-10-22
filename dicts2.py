d = dict(aaa=1, bbb=2, ccc=10)

del d["c" * 3]

print(d["ccc"])

# Por qué falla?
# Poner un pdb en la línea 4 y explorar el contenido de d
# y el valor de la expresion "c" * 3