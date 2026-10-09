producto1 = [101, "Teclado Logi", 120000.0, "Perifericos", 20]
producto2 = [102, "Notbook hp", 1300000.0, "Notebooks", 4]
producto3 = [103, "Mouse hp", 40000.0, "Perifericos", 80]

listaProductos = [producto1, producto2, producto3]

for producto in listaProductos:
    print("Codigo:", producto[0])
    print("Descripcion:", producto[1])
    print("Precio:", producto[2])
    print("Stock:", producto[4])
