
def seleccionarDeLista(lista, titulo, pregunta = "Elija una opción...", caracterTitulo = "-"  ):
    print()
    print(caracterTitulo * len(titulo))
    print(f"{titulo}")
    print(caracterTitulo * len(titulo))
    print()
    listaValidacion = []
    for i in range(len(lista)):
        print(f"{i+1}- {lista[i]}")
        listaValidacion.append(str(i+1))

    while True:
        opc = input(pregunta)
        if not(opc in listaValidacion):
            print("Opción Incorrecta, vuelva a intentarlo.")
        else:
            break
    print()
    return int(opc) - 1
