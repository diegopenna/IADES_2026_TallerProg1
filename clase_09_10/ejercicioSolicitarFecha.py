def solictarFecha(mensaje = "Ingrese Fecha (dd/mm/aaaa): "):
    valDias = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        fecha = input(mensaje)
        #validar que el formato sea ##/##/####
        
        if len(fecha) != 10:
            print("Formato de fecha incorrecto. Longitud incorrecta.")
            continue

        if not(fecha[2] in ["/", "-"] and fecha[5] in ["/", "-"]):
            print("Formato de fecha incorrecto. Caracter de separación invalido")
            continue

        dia = fecha[:2]
        mes = fecha[3:5]
        anio = fecha[-4:]

        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print("Formato de fecha incorrecto. Los campos día mes y año deben ser numericos")
            continue

        numDia = int(dia)
        numMes = int(mes)
        numAnio = int(anio)

        if not ( 1 <= numMes <= 12):
            print("Formato de fecha incorrecto. Número de mes incorrecto.")
            continue

        if esAnioBisiesto2(numAnio):
            valDias[1] = 29
        else:
            valDias[1] = 28

        if not (1 <= numDia <= valDias[numMes - 1]):
            print("Formato de fecha incorrecto. Número de dia incorrecto.")
            continue

# Otra opcion para validar el dia sin la lista de validacion
#        if numMes in [1, 3, 5, 7, 8, 10, 12]:
#            if not (1 <= numDia <= 31):
#                print("Formato de fecha incorrecto. Número de dia incorrecto.")
#                continue
#        elif numMes in [4, 6, 9, 11]:
#            if not (1 <= numDia <= 30):
#                print("Formato de fecha incorrecto. Número de dia incorrecto.")
#                continue


        break

    return f"{dia}/{mes}/{anio}"


def esAnioBisiesto(anio):
    #Tener en cuenta que un año es bisiesto si es divisible por 4, 
    #    excepto los años divisibles por 100, 
    #    que solo son bisiestos si además son divisibles por 400.
    if anio % 4 == 0:
        if anio % 100 == 0:
            return anio % 400 == 0
        else:
            return True
    else:
        return False

def esAnioBisiesto2(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False

print(solictarFecha())
