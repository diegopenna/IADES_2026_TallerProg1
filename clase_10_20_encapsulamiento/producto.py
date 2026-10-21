class Producto():
    def __init__(self, codigo, descripcion, precio, stock):
        self.set_codigo(codigo)
        self.set_descripcion(descripcion)
        self.set_precio(precio)
        self.set_stock(stock)

    def __str__(self):
        return(f"Codigo: {self.__codigo}\n" + 
               f"Descripcion: {self.__descripcion}\n"+
               f"Precio: {self.__precio}\n" +
               f"Stock: {self.__stock}")

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, valor):
        try:
            uncodigo = int(valor)
        except ValueError:
            raise ValueError("El codigo debe ser numerico.")

        if uncodigo <= 0:
            raise ValueError("El codigo debe ser mayor a cero")
        self.__codigo = uncodigo 

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, valor):
        if str(valor) == "":
            raise ValueError("La Descripcion no puede ser nula.")
        self.__descripcion = valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        try:
            unprecio = float(valor)
        except ValueError:
            raise ValueError("El precio debe ser numerico.")

        if unprecio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self.__precio = unprecio

    def get_stock(self):
        return self.__precio

    def set_stock(self, valor):
        try:
            unstock = int(valor)
        except ValueError:
            raise ValueError("El stock debe ser numerico.")
        if unstock < 0:
            raise ValueError("El stock debe ser mayor igual  a cero")
        self.__stock = unstock


prod = Producto(101, "Una computadora", 123456.78, 10)
print(prod)


print("Ingrese datos Producto:")
codigo = input("Coodigo:") 
descripcion = input("Descripcion:")
precio = input("Precio:")
stock = input("Stock:")

try:
    nuevoProducto = Producto(codigo, descripcion, precio, stock)
    print("Se creo el producto:")
    print(nuevoProducto)
except ValueError as err:
    print("Ocurrio un error al crear el producto")
    print(err)

print("Modificar Producto:")
print(nuevoProducto)
codigo = input("Coodigo:") 
descripcion = input("Descripcion:")
precio = input("Precio:")
stock = input("Stock:")

try:
    nuevoProducto.set_codigo(codigo)
    nuevoProducto.set_descripcion(descripcion)
    nuevoProducto.set_stock(stock)
    nuevoProducto.set_precio(precio)
except ValueError as err:
    print(err)






"""
prod.precio = -1000
prod.stock = "Cero"

print(prod)

prod.descripcion = "Otra Computadora"
"""

