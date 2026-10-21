class Producto():
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion =  descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return(f"Codigo: {self.__codigo}\n" + 
               f"Descripcion: {self.__descripcion}\n"+
               f"Precio: {self.__precio}\n" +
               f"Stock: {self.__stock}")

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        try:
            uncodigo = int(valor)
        except ValueError:
            raise ValueError("El codigo debe ser numerico.")

        if uncodigo <= 0:
            raise ValueError("El codigo debe ser mayor a cero")
        self.__codigo = uncodigo 

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if str(valor) == "":
            raise ValueError("La Descripcion no puede ser nula.")
        self.__descripcion = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        try:
            unprecio = float(valor)
        except ValueError:
            raise ValueError("El precio debe ser numerico.")

        if unprecio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self.__precio = unprecio

    @property
    def stock(self):
        return self.__precio

    @stock.setter
    def stock(self, valor):
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
    nuevoProducto.codigo = codigo
    nuevoProducto.descripcion = descripcion
    nuevoProducto.stock = stock
    nuevoProducto.precio = precio
except ValueError as err:
    print(err)

print(nuevoProducto.codigo)




"""
prod.precio = -1000
prod.stock = "Cero"

print(prod)

prod.descripcion = "Otra Computadora"
"""

