import utilidades as u
import datosiniciales

patentes = datosiniciales.patentes
descripciones = datosiniciales.descripciones
capacidades = datosiniciales.capacidades
categorias = datosiniciales.categorias
disponibles = datosiniciales.disponibles

listacategorias = datosiniciales.listacategorias


def menuPrincipal():
    while True:
        opc = u.mostrarMenu([
                    "Alta de Vehiculo", 
                    "Modificacion de Vehiculo", 
                    "Baja de Vehiculo", 
                    "Consulta de vehiculo",
                    "Listado de vehiculos",
                    "Salir"],
                    titulo="Menu de Vehículos")
        if opc == "1":
            altaVehiculo()
        elif opc == "2":
            modificarVehiculo()
        elif opc == "3":
            eliminarVehiculo()
        elif opc == "4":
            consultarVehiculo()
        elif opc == "5":
            mostrarListaVehiculos()
        else:
            break

def altaVehiculo():

    u.mostrarTitulo("Alta de Vehiculo")
    print("Datos del Vehiculo (vacío para cancelar):")
    try:
        unapatente = u.solicitarPatente("Patente: ")
        if buscarPatente(unapatente) >= 0:
            print("Ya existe una patente con ese numero.")
            return
        unadescripcion = u.solicitarTexto("Descripción: ", obligatorio=True)
        unacapacidad = u.solicitarDecimal("Capacidad (kg): ", valorMinimo=1)
        unacategoria = u.solicitarDeLista("Categoria: ", listacategorias)
        estadisponible = u.solicitarDeLista("Disponible: ", ["Si", "No"])
        #hasta aca valide los tipos de datos.
        #Ahora controlo que no este cargada esa patente.    

        patentes.append(unapatente)
        descripciones.append(unadescripcion)
        capacidades.append(unacapacidad)
        categorias.append(unacategoria)
        disponibles.append(estadisponible)

    except u.CanceladoPorUsuario:
        print("Operacion cancelada")

def modificarVehiculo():
    u.mostrarTitulo("Modificar Vehiculo")
    try:
        ipatente = solicitarPatenteExistente("Patente a modificar: ")

        unadescripcion = descripciones[ipatente]
        unacapacidad = capacidades[ipatente]
        unacategoria = categorias[ipatente]
        estadisponible = disponibles[ipatente]

        print(f"Descripcion Actual: {unadescripcion}")
        try:
            unadescripcion = u.solicitarTexto("Nueva Descripcion:", obligatorio=True)
        except u.CanceladoPorUsuario:
            pass
        
        print(f"Capacidad Actual: {unacapacidad}")
        try:
            unacapacidad = u.solicitarDecimal("Nueva Capacidad (kg): ", valorMinimo=1) 
        except u.CanceladoPorUsuario:
            pass

        print(f"Categoria Actual: {unacategoria}")
        try:
            unacategoria = u.solicitarDeLista("Nueva Categoria: ", listacategorias) 
        except u.CanceladoPorUsuario:
            pass

        print(f"Disponibilidad Actual: {estadisponible}")
        try:
            estadisponible = u.solicitarDeLista("Disponible: ", ["Si", "No"])
        except u.CanceladoPorUsuario:
            pass

        opc = u.solicitarDeLista("Confirmar operacion de Guardado: ", ["Si", "No"], permiteCancelar=False)
        if (opc == "Si"):
            descripciones[ipatente] = unadescripcion
            capacidades[ipatente] = unacapacidad
            categorias[ipatente] = unacategoria
            disponibles[ipatente] = estadisponible
        else:    
            print("Operacion cancelada")

    except u.CanceladoPorUsuario:
        print("Operacion cancelada")

def eliminarVehiculo():
    u.mostrarTitulo("Eliminar Vehiculo")
    try:

        ipatente = solicitarPatenteExistente("Patente a elimiar: ")
        
        opc = u.solicitarDeLista("Confirmar operacion de Eliminacion: ", ["Si", "No"], permiteCancelar=False)
        if (opc == "Si"):
            patentes.pop(ipatente)
            descripciones.pop(ipatente)
            capacidades.pop(ipatente)
            categorias.pop(ipatente)
            disponibles.pop(ipatente) 
        else:    
            print("Operacion cancelada")


    except u.CanceladoPorUsuario:
        print("Operacion cancelada")


def consultarVehiculo():
    try:
        ipatente = solicitarPatenteExistente()
        mostrarDatosVehiculo(ipatente)
    except u.CanceladoPorUsuario:
        print("Operacion cancelada")

def mostrarDatosVehiculo(indiceVehiculo):
    u.mostrarTitulo("Datos de Vehiculo")
    print(f"Patente: {patentes[indiceVehiculo]}")
    print(f"Descripción: {descripciones[indiceVehiculo]}")
    print(f"Canpacidad: {capacidades[indiceVehiculo]}")
    print(f"Categoria: {categorias[indiceVehiculo]}")
    print(f"Disponible: {disponibles[indiceVehiculo]}")
    print("*"*50)
    print()

def buscarPatente(patente):
    return u.buscarEnLista(patentes, patente)

def mostrarListaVehiculos():
    u.mostrarTitulo("Listado de  Vehiculos")

    if (len(patentes) == 0):
        print("No hay vehiculos cargados")
        return
    
    print(f"Patente | {'Descripcion':20} | {"Capacidad":15} | {"Categoria":15} | {"Disponible":10} ")
    print("-"*80)
    for i in range(len(patentes)):
        print(f"{patentes[i]:7} | {descripciones[i]:20} | {capacidades[i]:15,.2f} | {categorias[i]:^15} | {disponibles[i]:10}")

def solicitarPatenteExistente(mensaje = "Ingrese una patente:"):
        while True:
            unaPatente = u.solicitarPatente(mensaje)
            ipatente = buscarPatente(unaPatente) 
            if ipatente == -1:
                print("No existe una patente con ese numero.")
            else:
                print("Patente encontrada")
                return ipatente
    


menuPrincipal()