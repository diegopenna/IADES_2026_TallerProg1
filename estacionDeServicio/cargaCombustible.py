

import funcionesComunes

combustibles = ["Nafta Súper", "Nafta Premium", "Gasoil Súper", "Gasoil Premium"]
precios = [2000, 2200, 2100, 2300]
tiposPago = ["Efectivo", "Débito o transferencia", "Tarjeta Visa", "Tarjeta Mastercard"]



def solicitarCantLitros():
    while True:
        cant = float(input("Ingrese cantidad de lítros:"))
        if (cant <= 0):
            print("La cantidad debe ser mayor a cero, vuelva a intentarlo.")
        else:
            break
    return cant

def solicitarDatosApp():
    print("¿Es socio de la App?")
    while True:
        opc = input("Responda s/n....")
        if not(opc in ("s", "n")):
            print("Opción Incorrecta, vuelva a intentarlo.")
        else:
            break
    return (opc == "s")

def procesarDescuentoApp(esSocioApp, combustibleSelecc, importe):
    if (esSocioApp and combustibleSelecc in [1, 3]):
        descuentoApp = importe * 0.05
    else:
        descuentoApp = 0.0
    return descuentoApp


def procesarDescuentoPago(opcMedioPago, importe):
    if (opcMedioPago == 0):
        descuentoPago = importe * 0.1
    elif (opcMedioPago == 1):
        descuentoPago = 0.0
    elif (opcMedioPago == 2):
        descuentoPago = 0.2
        if (descuentoPago > 8000):
            descuentoPago = 8000
    else:
        descuentoPago = 0.15
    return descuentoPago

def mostrarResumenDeCompra(combustibleSelecc, cantLitros, importe, descuentoApp, medioPagoSelec, descuentoPago, total):
    print(f"Combustible seleccionado:\t{combustibles[combustibleSelecc]}")
    print(f"Cantidad de litros cargados:\t{cantLitros}")
    print(f"Precio por litro:\t{precios[combustibleSelecc]}")
    print(f"Importe inicial de la carga:\t{importe}")
    if (descuentoApp > 0):
        print("Se aplicó o no el beneficio de la App")
        print(f"Descuento obtenido por la App:\t{descuentoApp}")
    print(f"Medio de pago seleccionado\t{tiposPago[medioPagoSelec]}")
    print(f"Descuento obtenido por el medio de pago:\t{descuentoPago}")
    print(f"Total final a pagar:\t{total}")

def ingresar():
    combustibleSelecc = funcionesComunes.seleccionarDeLista(combustibles, "TIPO DE COMBUSTIBLE")
    cant = solicitarCantLitros()
    socioApp = solicitarDatosApp();
    importe = cant * precios[combustibleSelecc]
    descuentoApp = procesarDescuentoApp(socioApp, combustibleSelecc, importe)
    subtotal = importe - descuentoApp
    opcMedioDePago = funcionesComunes.seleccionarDeLista(tiposPago, "MEDIOS DE PAGO")
    descuentoPago = procesarDescuentoPago(opcMedioDePago, subtotal)

    total = subtotal - descuentoPago

    mostrarResumenDeCompra(combustibleSelecc, cant, importe, descuentoApp, opcMedioDePago, descuentoPago, total)


#realizarCarga()
