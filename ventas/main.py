from utilidades import mostrarMenu
from productos import Productos

misProductos = Productos()

while True:
    opc = mostrarMenu(["Alta de producto",
                "Modificación de producto",
                "Baja de producto",
                "Consulta de productos",
                "Lista de precios",
                "Productos por categoría",
                "Productos con bajo stock",
                "Salir"
                ],
                titulo="Menu Productos")

    if opc == "1":
        misProductos.mostrarAlta()
    elif opc == "2":
        misProductos.mostrarModificar()
    elif opc == "3":
        misProductos.mostrarBaja()
    elif opc == "4":
        misProductos.mostrarConsultar()
    elif opc == "5":
        misProductos.mostrarListaDePrecios()
    elif opc == "6":
        misProductos.mostrarProductosPorCategoria()
    elif opc == "7":
        misProductos.mostrarProductosBajoStock()
    else:
        break