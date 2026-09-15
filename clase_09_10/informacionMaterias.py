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
    try:
        promedio = sum(lista) / len(lista)
        return promedio
    except ZeroDivisionError:
        return 0.0
    except Exception:
        return "Error desconocido"

def mostrarInformeMateria(codigo):
    try:
        nombreMateria = obtenerNombreMateria(codigo)
        notasMateria = obtenerNotasMateria(codigo)
        promedioMateria = calcularPromedioMateria(codigo)

        print(f"Informe de la materia: {nombreMateria}")
        print(f"Notas: {notasMateria}")
        print(f"Promedio: {promedioMateria}")
    except IndexError:
        print("No existe materia con ese código")



def main():
    try:
        codigo = input("Ingrese codigo de materia: ")
        codigo = int(codigo)
    except ValueError:
        print(f"El codigo de la materia no puede ser {codigo}. Tiene que ser numerico")
    else:
        if codigo < 1:
            print("El codigo debe ser mayor a 0")
        else:     
            mostrarInformeMateria(codigo)

try:
    main()
except Exception:
    #Guardo en una base el log del error
    #Enviar mail a los administradores
    print("Se produjo un error inesperado. Comuniquese con sistemas.")

#print(calcularPromedio([]))

