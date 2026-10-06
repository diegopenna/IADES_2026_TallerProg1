class Producto:
    codigo:int
    descripcion:str
    stock:int
    precio:float

    def descontarStock(self, cantidad):
        if (self.stock >= cantidad):
            self.stock = self.stock - cantidad
            return True
        else:
            return False


producto1 = Producto()
producto1.codigo = 101
producto1.descripcion = "Teclado Logi"
producto1.precio = 80.0
producto1.stock = 10
print("Stock anterior:", producto1.stock)

cantidad = int(input("Ingrese una cantidad: "))

if producto1.descontarStock(cantidad):
    print("Nuevo stock:", producto1.stock)
else:
    print("No se pudo descontar el stock solicitado.")

producto1.descontarStock(3)
print("Nuevo stock:", producto1.stock)
