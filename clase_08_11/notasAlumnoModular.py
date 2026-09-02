
def moduloPrincipal():
    unasNotas = ingresoNotas()
    unPromedio = calculoPromedio(unasNotas) 
    unEstado = calcularEstado(unPromedio)
    mostrarInforme(unEstado)

    otroPromedio = calculoPromedio([2,3,4])
    print(otroPromedio)


def ingresoNotas():
    #ingreso de notas
    notas = []
    while True:
        nota = input("Ingrese Nota (vacio para cancelar):")
        if (nota == ""):
            break
        notas.append(int(nota))

    return notas

#Definicion Funcion calculoPromedio
def calculoPromedio(notas):
    suma = 0
    for i in range(len(notas)):
        suma = suma + notas[i]
    promedio = suma / len(notas)
    return promedio

def calcularEstado(promedio):
    if promedio >= 7:
        estado = "Promocionado"
    elif promedio >= 4:
        estado = "Aprobado sin promoción"
    else:
        estado = "Desaprobado"
    return estado

def mostrarInforme(estado):
    print("Informe del alumno")
    print("------------------")
    print("Estado:", estado)


moduloPrincipal()
