
def mostrarMenu(opciones: list, valores : list = None, titulo:str = None,   pregunta:str = "Elija una opcion:"):
    if titulo != None and titulo != "":
        mostrarTitulo(titulo)

    if valores == None:
        valores = []
        for i in range(len(opciones)):
            valores.append(str(i + 1))

    for i in range(len(opciones)):
        print(valores[i], '-' ,  opciones[i])
    while True:
        opc = input(pregunta)
        if opc in valores:
            break
        else:
            print("Opcion incorrecta.")
    return opc


def solicitarDecimal(mensaje, valorMinimo = None, valorMaximo = None):
    while True:
        try:
            num = float(input(mensaje))

            if valorMinimo != None and num < valorMinimo:
                print(f"El valor debe ser mayor o igual a {valorMinimo}.")
            elif valorMaximo !=  None and num > valorMaximo:
                print(f"El valor debe ser menor o igual a {valorMaximo}.")
            else:
                break
        except ValueError:
            print(f"Debe ingrersar un numero valido.")
    return num

def solicitarEntero(mensaje, valorMinimo = None, valorMaximo = None):
    num = solicitarDecimal(mensaje, valorMinimo, valorMaximo)
    return int(num)

def solicitarPatente(mensaje = "Patente: "):
    while True:
        valor = input(mensaje)
        if 6 <= len(valor)  <= 7:
            return valor.upper()
        else:
            print("Formato de patente incorrecto.")

def mostrarTitulo(titulo):
    print()
    print("-"*len(titulo))
    print(titulo)
    print("-"*len(titulo))
    print()
