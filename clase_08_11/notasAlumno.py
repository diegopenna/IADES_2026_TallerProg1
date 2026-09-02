
#ingreso de notas
notas = []
while True:
    nota = input("Ingrese Nota (vacio para cancelar):")
    if (nota == ""):
        break
    notas.append(int(nota))

suma = 0
for i in range(len(notas)):
    suma = suma + notas[i]
promedio = suma / len(notas)

if promedio >= 7:
    estado = "Promocionado"
elif promedio >= 4:
    estado = "Aprobado sin promoción"
else:
    estado = "Desaprobado"

print("El estado del alumno es:", estado)


