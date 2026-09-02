import funcionesComunes
import cargaCombustible
import gomeria
import lubricentro
import confiteria

menuPrincipal = ["Carga de Combustible", "Lubricentro", "Gomeria", "Confiteria", "Salir"]

while True:
    opc = funcionesComunes.seleccionarDeLista(menuPrincipal,
                    "SISTEMA DE ESTACION DE SERVICIO YFP")
    if (opc == 0):
        cargaCombustible.ingresar()
    if (opc == 1):
        lubricentro.ingresar()
    if (opc == 2):
        gomeria.ingresar()
    if (opc == 3):
        confiteria.ingresar()
    if (opc == 4):
        break
