class Libro:
    codigo: int
    titulo: str
    autor: str
    anio: int
    disponible: bool


"""
libro1 	101	El Principito	Antoine de Saint-Exupéry	1943	Sí
libro2	102	1984	George Orwell	1949	Sí
libro3	103	Rayuela	Julio Cortázar	1963	No
"""
libro1 = Libro()
libro1.codigo = 101
libro1.titulo = "El Principito"
libro1.autor = "Antoine de Saint-Exupéry"
libro1.anio = 1943
libro1.disponible = True

libro2 = Libro()
libro2.codigo = 102
libro2.titulo = "1984"
libro2.autor = "George Orwell"
libro2.anio = 1949
libro2.disponible = True

libro3 = Libro()
libro3.codigo = 103
libro3.titulo = "Rayuela"
libro3.autor = "Julio Cortázar"
libro3.anio = 1963
libro3.disponible = False


