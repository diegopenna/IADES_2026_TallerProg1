from producto import Producto
from productos import Productos

misProductos = Productos()

prod = Producto(101, "Notebook Lenovo IdeaPad", "Computadoras", 990000, 5)
misProductos.agregar(prod)
prod = Producto(102,  "Notebook HP 15", "Computadoras", 1100000, 3)
misProductos.agregar(prod)
misProductos.agregar(Producto(103,	"Monitor Samsung 24\"", "Monitores", 190000, 8))

misProductos.mostrarLista()
print("Cantidad productos:", len(misProductos.obtenerListaProductos()))
print("Cantidad productos:", misProductos.cantidadProductos)

misProductos.cantidadProductos = 4