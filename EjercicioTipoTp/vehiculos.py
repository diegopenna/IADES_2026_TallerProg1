import utilidades as u

patentes = []
descripciones = []
capacidades = []
categorias = []
disponibles = []

listacategorias = ["Auto", "Camion", "Camioneta", "Moto"]

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
            print("Consulta de vehiculo")
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
        unaPatente = u.solicitarPatente("Patente a modificar: ")
        ipatente = buscarPatente(unaPatente) 
        if ipatente == -1:
            print("No existe una patente con ese numero.")
            return

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
        unaPatente = u.solicitarPatente("Patente a elimiar: ")
        ipatente = buscarPatente(unaPatente) 
        if ipatente == -1:
            print("No existe una patente con ese numero.")
            return
        else:
            print("Patente encontrada")
        
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


def buscarPatente(patente):
    return u.buscarEnLista(patentes, patente)

def mostrarListaVehiculos():
    for i in range(len(patentes)):
        print("Patente: ", patentes[i])
        print("Descripcion: ", descripciones[i])
        print("Capacidad: ", capacidades[i])
        print("Categoria: ", categorias[i])
        print("Disponible: ", disponibles[i])

menuPrincipal()