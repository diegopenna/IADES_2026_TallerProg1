class Producto:
    def __init__(self,codigo:int, descripcion:str, precio:float, stock:int):
        self.codigo = codigo
        self.descripcion = descripcion
        self.stock = stock
        self.precio = precio



    def descontarStock(self, cantidad):
        if (self.stock >= cantidad):
            self.stock = self.stock - cantidad
            return True
        else:
            return False


producto1 = Producto(101,"Teclado Logi", 80.0, 10)

print("Stock anterior:", producto1.stock)

cantidad = int(input("Ingrese una cantidad: "))

if producto1.descontarStock(cantidad):
    print("Nuevo stock:", producto1.stock)
else:
    print("No se pudo descontar el stock solicitado.")

producto1.descontarStock(3)
print("Nuevo stock:", producto1.stock)
