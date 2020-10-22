lista = []

def bar():
    lista.append("x")
    print(lista)

def bar2():
    lista += ["x"]
    print(lista)


bar()
bar2()

# Por que el primero anda y el segundo no?