class Producto():
    def __init__(self, codigo, descripcion, precio, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return(f"Codigo: {self.codigo}\n" + 
               f"Descripcion: {self.descripcion}\n"+
               f"Precio: {self.precio}\n" +
               f"Stock: {self.stock}")



prod = Producto(101, "Una computadora", 123456.78, 10)

print(prod)

print()
prod = Producto(-101, "", -123456.78, -10)
print(prod)