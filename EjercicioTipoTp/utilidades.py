class CanceladoPorUsuario(Exception):
    pass

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


def solicitarDeLista(mensaje, valores, permiteCancelar = True):
    print(mensaje)
    for i in range(len(valores)):
        print(f"{i + 1} - {valores[i]}")

    opc = solicitarDecimal("Elija una opción: ", 1, len(valores), permiteCancelar)
    seleccion = valores[int(opc) - 1]
    print(f"Valor seleccionado: {seleccion}")
    return valores[int(opc) - 1]

    

def solicitarTexto(mensaje, obligatorio = False, limpiarEspacios = True, permiteCancelar = True):
    while True:
        valor = input(mensaje)

        if permiteCancelar and valor.strip() == "":
            opc = input("Esta seguro que desea cancelar (s, n): ")
            if opc == "s":
                raise(CanceladoPorUsuario)

        
        if obligatorio == True and valor.strip() == "":
            print("El campo es obligatorio")
        else:
            break
    if limpiarEspacios:            
        return valor.strip()
    else:
        return valor

def solicitarDecimal(mensaje, valorMinimo = None, valorMaximo = None, permiteCancelar = True):
    while True:
        try:
            num = float(solicitarTexto(mensaje, permiteCancelar=permiteCancelar))

            if valorMinimo != None and num < valorMinimo:
                print(f"El valor debe ser mayor o igual a {valorMinimo}.")
            elif valorMaximo !=  None and num > valorMaximo:
                print(f"El valor debe ser menor o igual a {valorMaximo}.")
            else:
                break
        except ValueError:
            print(f"Debe ingrersar un numero valido.")
    return num

def solicitarEntero(mensaje, valorMinimo = None, valorMaximo = None, permiteCancelar = True):
    num = solicitarDecimal(mensaje, valorMinimo, valorMaximo, permiteCancelar)
    return int(num)

def solicitarPatente(mensaje = "Patente: ", permiteCancelar = True):
    while True:
        valor = solicitarTexto(mensaje, permiteCancelar=permiteCancelar)
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

def buscarEnLista(lista, valor):
    for i in range(len(lista)):
        if (str(valor).lower() == str(lista[i]).lower()):
            return i
    return -1