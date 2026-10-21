from utilidades import mostrarPresioneParacontinuar
from producto import Producto

class Productos:
    def __init__(self):
        self.__listaProductos = []

    def obtenerListaProductos(self):
        return self.__listaProductos

    @property
    def cantidadProductos(self):
        return len(self.__listaProductos)

    def agregar(self, producto:Producto):
        self.__listaProductos.append(producto)

    def mostrarLista(self):
        for prod in self.__listaProductos:
            print(prod)

    def mostrarAlta(self):
        print("Alta de producto")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()

    def mostrarModificar(self):
        print("Modificación de producto")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()

    def mostrarBaja(self):
        print("Baja de producto")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()

    def mostrarConsultar(self):
        print("Consulta de producto")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()

    def mostrarListaDePrecios():
        print("Lista de precios")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()

    def mostrarProductosPorCategoria():
        print("Productos por categoría")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()

    def mostrarProductosBajoStock():
        print("Productos con bajo stock")
        print("##### funcionalidad en desarrollo #####")
        mostrarPresioneParacontinuar()
