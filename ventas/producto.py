from  utilidades import mostrarTitulo

class Producto:
    def __init__(self, codigo = 0, descripcion  = "", categoria = "", precio = 0.0, stock = 0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (f"Producto: {self.codigo} - {self.descripcion} ({self.categoria}) . Precio: {self.precio}")

    def mostrar(self):
        mostrarTitulo("Destalle de Producto")
        print(f"{self.codigo} - {self.descripcion}")
        print(f"Precio: {self.precio}")
        print(f"Categoria: {self.categoria}")
        print(f"Stock: {self.stock}")
        print()

"""
prod = Producto(101, "Notebook Lenovo IdeaPad", "Computadoras", 990000, 5)
print("print(prod):")
print(prod)
print("prod.mostrar():")
prod.mostrar()

"""
