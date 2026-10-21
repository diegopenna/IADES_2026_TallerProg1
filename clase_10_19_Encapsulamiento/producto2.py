class Producto():
    def __init__(self, codigo, descripcion, precio, stock):

        try:
            uncodigo = int(codigo)
        except ValueError:
            raise ValueError("El codigo debe ser numerico.")

        if uncodigo <= 0:
            raise ValueError("El codigo debe ser mayor a cero")
        self.codigo = uncodigo


        if str(descripcion) == "":
            raise ValueError("La Descripcion no puede ser nula.")
        self.descripcion = descripcion

        try:
            unprecio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser numerico.")

        if unprecio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self.precio = unprecio

        try:
            unstock = int(stock)
        except ValueError:
            raise ValueError("El stock debe ser numerico.")
        if unstock < 0:
            raise ValueError("El stock debe ser mayor igual  a cero")
        self.stock = unstock

    def __str__(self):
        return(f"Codigo: {self.codigo}\n" + 
               f"Descripcion: {self.descripcion}\n"+
               f"Precio: {self.precio}\n" +
               f"Stock: {self.stock}")



prod = Producto(101, "Una computadora", 123456.78, 10)

print(prod)

print()

prod = Producto("102", "Otra Computadora", 123456.78, 10)

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

stock = input(f"Ingrese un nuevo stock de {nuevoProducto.descripcion}: ")
nuevoProducto.stock = stock
print(nuevoProducto)

#Solo proteje atributos en el constructor
#Falla que no proteje los atributos cuando los accedo directamente

