def solictarFecha(mensaje = "Ingrese Fecha (dd/mm/aaaa): "):
    valDias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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

        if not (1 <= numDia <= valDias[numMes - 1]):
            print("Formato de fecha incorrecto. Número de dia incorrecto.")
            continue

        
        

        break

    return f"{dia}/{mes}/{anio}"


print(solictarFecha())