class Libro:
    estadoRoto:str = "Roto"
    estadoPrestado:str =  "Prestado"
    estadoDisponible:str = "Disponible"

    def __init__(self):
        self.codigo:int = 0
        self.titulo:str = ""
        self.autor:str = ""
        self.anio:int = 0
        self.estado:str = self.estadoDisponible

    def mostrarLibro(self):
        print("Libro:",self.codigo, "-",  self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.anio)
        print("Disponible:", self.disponible())     

    def disponible(self):
        return (self.estado == self.estadoDisponible)

    def prestar(self):

        if self.disponible():
            self.estado = self.estadoPrestado
            print("Se realizó el prestamo del Libro",self.codigo)  
        else:
            print("El libro", self.codigo ,"se encuentra", self.estado)


libro1 = Libro()
libro2 = Libro()
libro3 = Libro()

libro1.codigo = 101
libro1.titulo = "El Principito"
libro1.autor = "Antoine de Saint-Exupéry"
libro1.anio = 1943
libro1.estado = Libro.estadoDisponible

libro2.codigo = 102
libro2.titulo = "1984"
libro2.autor = "George Orwell"
libro2.anio = 1949
libro2.estado = Libro.estadoDisponible

libro3.codigo = 103
libro3.titulo = "Rayuela"
libro3.autor = "Julio Cortázar"
libro3.anio = 1963
libro3.estado = Libro.estadoRoto




libro3.prestar()