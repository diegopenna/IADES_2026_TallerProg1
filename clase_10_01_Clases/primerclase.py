class Producto:
    codigo:int
    descripcion:str
    precio:float
    categoria:str
    stock:int

print("Programa principal")

producto1 = Producto()
producto1.codigo = 101
producto1.descripcion = "Notebook Lenovo IdeaPad"
producto1.precio = 990000.0
producto1.categoria = "Computadoras"
producto1.stock = 5

print(producto1.codigo)
print(producto1.descripcion)
print(producto1.precio)
print(producto1.categoria)
print(producto1.stock)

producto2 = Producto()
producto2.codigo = 102
producto2.descripcion = "Notebook HP 15"
producto2.precio = 1100000.0
producto2.categoria = "Computadoras"
producto2.stock = 3

productos = []
productos.append(producto1)
productos.append(producto2)


for prod in productos:
    print(prod.codigo, prod.descripcion, prod.precio, prod.categoria, prod.stock)