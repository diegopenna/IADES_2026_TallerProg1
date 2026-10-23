from utilidades import mostrarPresioneParacontinuar, mostrarTitulo,solicitarTexto,CanceladoPorUsuario,solicitarDecimal, solicitarEntero, solicitarDeLista
from producto import Producto
from datosIniciales import  lista as listaInicialProductos

class Productos:

    def __init__(self):
        self.__listaProductos = listaInicialProductos
        self.__categorias = [        
                "Computadoras",
                "Monitores",
                "Periféricos",
                "Componentes",
                "Almacenamiento",
                "Redes",
                "Accesorios"]

    def obtenerListaProductos(self):
        return self.__listaProductos

    @property
    def cantidadProductos(self):
        return len(self.__listaProductos)

    def agregar(self, producto:Producto):
        if (producto.codigo == 0):
            producto.codigo = self.proximoCodigo()
        self.__listaProductos.append(producto)

    def proximoCodigo(self):
        codigoMax = 0
        for producto in self.__listaProductos:
            producto:Producto
            if (producto.codigo > codigoMax):
                codigoMax = producto.codigo

        return codigoMax + 1

    def mostrarLista(self):
        for prod in self.__listaProductos:
            print(prod)

    def mostrarAlta(self):
        mostrarTitulo("Alta de producto")
        try:

            print("Ingrese datos del producto")
            unadescripcion = solicitarTexto("Descripción: ", obligatorio=True)
            unprecio = solicitarDecimal("Precio: ", valorMinimo=0)
            unacategoria = solicitarDeLista("Categoria: ", self.__categorias)
            unstock = solicitarEntero("Stock: ",  valorMinimo=0)

            nuevoProducto = Producto(0, unadescripcion, unacategoria, unprecio, unstock)

            print("Usted esta a punto de agregar este producto:")
            nuevoProducto.mostrar()
            opc = solicitarDeLista("Desea continuar?", ["Si", "No"])
            if opc == "Si":
                self.agregar(nuevoProducto)
            else:
                print("No se agrego el producto.")

        except CanceladoPorUsuario:
            print("Operacion cancelada por el usuario.")

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
        mostrarTitulo("Consulta de productos")
        for producto in self.__listaProductos:
            producto:Producto
            print(producto)
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
