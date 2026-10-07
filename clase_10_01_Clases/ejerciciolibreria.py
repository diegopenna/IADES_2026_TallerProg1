class Libro:
    codigo: int
    titulo: str
    autor: str
    anio: int
    disponible: bool

    def mostrarLibro(self):
        print("Libro:",self.codigo, "-",  self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.anio)
        print("Disponible:", self.disponible)     

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Se realizó el prestamo del Libro",self.codigo)  
        else:
            print("El libro", self.codigo ,"no se encuentra disponible.")


"""
libro1 	101	El Principito	Antoine de Saint-Exupéry	1943	Sí
libro2	102	1984	George Orwell	1949	Sí
libro3	103	Rayuela	Julio Cortázar	1963	No
"""
libro1 = Libro()
libro2 = Libro()
libro3 = Libro()

libro1.codigo = 101
libro1.titulo = "El Principito"
libro1.autor = "Antoine de Saint-Exupéry"
libro1.anio = 1943
libro1.disponible = True

libro2.codigo = 102
libro2.titulo = "1984"
libro2.autor = "George Orwell"
libro2.anio = 1949
libro2.disponible = True

libro3.codigo = 103
libro3.titulo = "Rayuela"
libro3.autor = "Julio Cortázar"
libro3.anio = 1963
libro3.disponible = False

#punto 3
libros = []
libros.append(libro1)
libros.append(libro2)
libros.append(libro3)

print("Recorro por indice")
for i in range(len(libros)):
    print(libros[i].codigo, libros[i].titulo, libros[i].autor)

print()
print("Recorro por objeto")
for libro in libros:
    print(libro.codigo, libro.titulo, libro.autor)

#punto 4
 
def mostrarLibro(libro:Libro):
    print("Libro:",libro.codigo, "-",  libro.titulo)
    print("Autor:", libro.autor)
    print("Año:", libro.anio)
    print("Disponible:", libro.disponible)

print()
print("Recorro por objeto y llamo a la funcion")
for libro in libros:
    print()
    mostrarLibro(libro)


#punto 5

print()
print("Recorro por objeto y llamo al metodo del objeto libro")

for libro in libros:
    print()
    libro:Libro #es opcional, es solo para indicar que es el tipo libro
    libro.mostrarLibro()


#punto 6

"""
Prestar libro1.
Intentar prestar nuevamente libro1.
Intentar prestar libro3.
"""
print("")
print("Prestar libro1.")
libro1.prestar()
print("\nIntentar prestar nuevamente libro1.")
libro1.prestar()
print("")
print("Intentar prestar libro3.")
libro3.prestar()


