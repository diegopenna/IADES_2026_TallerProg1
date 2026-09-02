def mostrarMenu(titulo, *comida, separador = "-" ):
    print(titulo)
    print(separador * len(titulo))
    for i in range(len(comida)):
        print(comida[i])

mostrarMenu("Menu del dia", 
            "Fideos con tuco", 
            "Milanesa con fritas", 
            "Hamburguesas", 
            "Pescado con pure", 
            "Vacio con papas", 
            separador="*"
             )
print()
print("Diego", "Fernando", "Penna",sep=",",end="@")
print("Pepe")