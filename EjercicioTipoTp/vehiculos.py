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
            print("Modificacion de Vehiculo")
        elif opc == "3":
            print("Baja de Vehiculo")
        elif opc == "4":
            print("Consulta de vehiculo")
        elif opc == "5":
            mostrarListaVehiculos()
        else:
            break

def altaVehiculo():

    u.mostrarTitulo("Alta de Vehiculo")
    print("Datos del Vehiculo:")
    unapatente = u.solicitarPatente("Patente: ")
    unadescripcion = input("Decripcion: ")
    unacapacidad = u.solicitarDecimal("Capacidad (kg): ")
    unacategoria = input("Categoria: ")
    estadisponible = input("Disponible (s,n): ")

    patentes.append(unapatente)
    descripciones.append(unadescripcion)
    capacidades.append(unacapacidad)
    categorias.append(unacategoria)
    disponibles.append(estadisponible)

def mostrarListaVehiculos():
    for i in range(len(patentes)):
        print("Patente: ", patentes[i])
        print("Descripcion: ", descripciones[i])
        print("Capacidad: ", capacidades[i])
        print("Categoria: ", categorias[i])
        print("Disponible: ", disponibles[i])

menuPrincipal()