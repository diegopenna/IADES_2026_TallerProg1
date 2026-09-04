cadena = "Hola a todos"

print(cadena[1])
print(len(cadena))

for i in range(len(cadena)):
    print(cadena[i])
print("Indice negativo")
print(cadena[-1])
print(cadena[-2])
print(cadena[-3])
print(cadena[-12])

lista = ["Azucar", "Leche", "Arroz", "Manteca"]

print(lista[2])
print(lista[-1])

#subcadenas
print("SUBCADENAS")
print(cadena[0:3])
print(cadena[:3])
print(cadena[0:10:1])
print(cadena[0:10:2])
print(cadena[0:10:3])
print(cadena[::2])

print(cadena[-12:-11])
print(cadena[-3:])