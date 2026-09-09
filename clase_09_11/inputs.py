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

def solicitarCUIT(mensaje = "Ingrese el CUIT:"):
    #ASEGURARME QUE RETORNE UN CODIGO ##-########-#
    #el usario ingresa ########### devuelve ##-########-#
    valid_pref = [20, 27, 23, 24, 25 ,26, 30, 33, 34]
    while True:
        cuit = input(mensaje)

        if len(cuit) == 11:
            prefijo = cuit[0:2]
            dni= cuit[2:10]
            verif= cuit[-1]
        elif len(cuit) == 13:
            prefijo = cuit[0:2]
            dni= cuit[3:11]
            verif = cuit[-1]
            if cuit[2] != "-" or cuit[-2] != "-":
                print("Formato de Cuit incorrecto.")
                continue    
        else:
            print("Longitud Incorrecta..")
            continue

        #Si llego aca valido prefijo
        try:
            if not (int(prefijo) in valid_pref):
                print("El Prefijo tiene un valor incorrecto.")
                print("Valores posibles:", valid_pref )
                continue
        except ValueError:
            print("El prefijo debe ser un número.")
            continue

        #Si llego aca valido si dni es numero.
        if not dni.isdigit():
            print("El DNI debe ser un número.")
            continue

        if not verif.isdigit():
            print("El Dígito verificador debe ser un número.")
            continue
        

        break

    return f"{prefijo}-{dni}-{verif}"
        


