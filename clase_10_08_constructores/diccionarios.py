productos = [
    {
    "codigo" : 101, 
    "descripcion": "Teclado Logi",
    "precio" : 120000.0, 
    "categoria": "Perifericos", 
    "stock": 20
    },
    {
    "codigo" : 102, 
    "descripcion": "Monitor",
    "precio" : 330000.0, 
    "categoria": "Perifericos", 
    "stock": 50
    },
    {
    "descripcion": "Noteboo hp",
    "codigo" : 103, 
    "precio" : 12000000.0, 
    "categoria": "NOtebooks", 
    "stock": 5
    }
    ]


def mostrarProducto(producto):
    for clave, valor in producto.items():
        print(f"{clave}: {valor}")

for unproducto in productos:
    mostrarProducto(unproducto)
