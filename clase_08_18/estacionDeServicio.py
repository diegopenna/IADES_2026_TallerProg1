combustibles = ["Nafta Súper", "Nafta Premium", "Gasoil Súper", "Gasoil Premium"]
precios = [2000, 2200, 2100, 2300]

print("TIPO DE COMBUSTIBLE\n")
for i in range(len(combustibles)):
    print(f"{i+1}- {combustibles[i]}")

while True:
    opc = input("Elia una opción..")
    if not(opc in ("1", "2", "3", "4")):
        print("Opción Incorrecta, vuelva a intentarlo.")
    else:
        break

combustibleSelecc = int(opc) - 1

while True:
    cant = float(input("Ingrese cantidad de lítros:"))
    if (cant <= 0):
        print("La cantidad debe ser mayor a cero, vuelva a intentarlo.")
    else:
        break
    

print("¿Es socio de la App?")
while True:
    opc = input("Responda s/n....")
    if not(opc in ("s", "n")):
        print("Opción Incorrecta, vuelva a intentarlo.")
    else:
        break

importe = cant * precios[combustibleSelecc]

socioApp = (opc == "s");

if (combustibleSelecc in [1, 3]):
    descuentoApp = importe * 0.05
else:
    descuentoApp = 0.0

print("MEDIO DE PAGO\n")
print("1 - Efectivo\n2 - Débito o transferencia\n3 - Tarjeta Visa\n4 - Tarjeta Mastercard")
while True:
    opc = input("Elia una opción..")
    if not(opc in ("1", "2", "3", "4")):
        print("Opción Incorrecta, vuelva a intentarlo.")
    else:
        break
subtotal = importe - descuentoApp

if (opc == "1"):
    descuentoPago = subtotal * 0.1
    medioPagoSelec = "Efectivo"
elif (opc == "2"):
    descuentoPago = 0.0
    medioPagoSelec = "Débito o transferencia"
elif (opc == "3"):
    descuentoPago = 0.2
    if (descuentoPago > 8000):
        descuentoPago = 8000
    medioPagoSelec = "Tarjeta Visa"
else:
    descuentoPago = 0.15
    medioPagoSelec = "Tarjeta Mastercard"

total = subtotal - descuentoPago

print(f"Combustible seleccionado:\t{combustibles[combustibleSelecc]}")
print(f"Cantidad de litros cargados:\t{cant}")
print(f"Precio por litro:\t{precios[combustibleSelecc]}")
print(f"Importe inicial de la carga:\t{importe}")
if (descuentoApp > 0):
    print("Se aplicó o no el beneficio de la App")
    print(f"Descuento obtenido por la App:\t{descuentoApp}")
print(f"Medio de pago seleccionado\t{medioPagoSelec}")
print(f"Descuento obtenido por el medio de pago:\t{descuentoPago}")
print(f"Total final a pagar:\t{total}")
