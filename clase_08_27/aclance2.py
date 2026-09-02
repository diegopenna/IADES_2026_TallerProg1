ultimoAcceso = "No Definido"

def controlarAcceso(nombreUsuario, password):
    # Hace lo que tiene que hacer#
    accesoOk = True
    global ultimoAcceso
    ultimoAcceso = nombreUsuario
    print("Bienvenido:", ultimoAcceso)
    return accesoOk



if (controlarAcceso("dpenna", "123456")):
    print("Usuario actual:", ultimoAcceso)
