contador = 0
def calcularImporteFinal(precio):
    global contador
    contador = contador + 1
    impuesto = precio * iva
    total = precio + impuesto
    return total

iva = 0.105
precio = 1000

importeFinal = calcularImporteFinal(precio)
print("Calculo nro:", contador)
print("Precio:", precio)
print("Iva:", iva)
print("Imprte final:", importeFinal)


importeFinal = calcularImporteFinal(500)

print("Otro Calculo")

print("Calculo nro:", contador)
print("Precio:", precio)
print("Iva:", iva)
print("Imprte final:", importeFinal)
