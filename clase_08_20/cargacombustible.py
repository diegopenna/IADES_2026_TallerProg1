combustibles = ["Nafta Súper", "Nafta Premium", "Gasoil Súper", "Gasoil Premium"]
precios = [2000, 2200, 2100, 2300]

tipospago =["Efectivo", "Débito o transferencia", "Tarjeta Visa", "Tarjeta Mastercard"]

print("Tipo de Combustible")
for i in range(len(combustibles)):
    print(f"{i + 1}- {combustibles[i]}")

while True:
    opc = input("Ingrese una opcion...")
    if (opc in ["1", "2", "3", "4"]):
        break
    else:
        print("Opcion Incorrecta")

indice = int(opc) - 1

while True:
    litros = float(input("Litros cargados:"))
    if litros > 0:
        break
    else:
        print("El valor debe ser mayor a 0")

importe = litros * precios[indice]

print("\nEsta carga:")
print(f"Tipo de Combustible: {combustibles[indice]}")
print(f"Cantidad de litros: {litros}")
print(f"Precio por litro: {precios[indice]}")
print(f"Importe: {importe}")

while True:
    opc = input("Es socio de la app (s/n)...")
    if (opc in ["s", "n"]):
        break
    else:
        print("Opcion incorrecta")


essocio = (opc == "s")
espremiun = (indice in [1, 3])

descuentoapp = 0.0
if essocio and espremiun:
    descuentoapp = importe * 0.05

subtotal = importe - descuentoapp

if (descuentoapp > 0):
    print(f"Descuento por app: {descuentoapp}")

print(f"Subtotal: {subtotal}")

print("\nSeleccione medio de pago:")
for i in range(len(tipospago)):
    print(f"{i + 1}- {tipospago[i]}")
while True:
    opc = input("Ingrese una opcion...")
    if (opc in ["1", "2", "3", "4"]):
        break
    else:
        print("Opcion Incorrecta")

print()
indicepago = int(opc) -1
if (indicepago == 0):
    #Efictivo
    descpago = subtotal * 0.1
elif (indicepago == 1):
    #transf
    descpago = 0.0
elif (indicepago == 2):
    #visa
    descpago = subtotal * 0.2
    if descpago > 8000:
        descpago = 8000.0
else:
    descpago = subtotal * 0.15

print(f"Tipo de pago seleccionado: {tipospago[indicepago]}")

total = subtotal - descpago

print(f"Descuento por tipo de pago: {descpago}")
print(f"\nTOTAL A PAGAR: {total}")
