materias = [
    "Fundamentos de Programacion", 
    "Programacion 1", 
    "Matematicas", 
    "Sistemas operativos"
    ]
notas = [
    [9, 7, 2, 6],
    [],
    [5, 7],
    [4, 5, 6, 7, 8, 9]
]

def obtenerNombreMateria(codigo):
    return materias[codigo - 1]

def obtenerNotasMateria(codigo):
    return notas[codigo - 1]

def calcularPromedioMateria(codigo):
    notasMateria = obtenerNotasMateria(codigo)
    return calcularPromedio(notasMateria)

def calcularPromedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio

def mostrarInformeMateria(codigo):
    nombreMateria = obtenerNombreMateria(codigo)
    notasMateria = obtenerNotasMateria(codigo)
    promedioMateria = calcularPromedioMateria(codigo)

    print(f"Infrome de la materia: {nombreMateria}")
    print(f"Notas: {notasMateria}")
    print(f"Promedio: {promedioMateria}")

def main():
    codigo = int(input("Ingrese codigo de materia: "))
    mostrarInformeMateria(codigo)

try:
    main()
except ValueError:
    print("Debe igresar un numero")
except IndexError:
    print("Codigo inexistente")
except ZeroDivisionError:
    print("No hay notas para la materia")