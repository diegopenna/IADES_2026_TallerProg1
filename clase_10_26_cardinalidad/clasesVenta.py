class Cliente():
    def __init__(self, codigo:int, cuit:str):
        self.codigo = codigo
        self.cuit = cuit

class Persona(Cliente):
    def __init__(self, codigo:int, cuit:str, nombre:str, apellido:str, dni:int):
        super().__init__(codigo, cuit)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Empresa(Cliente):
    def __init__(self, codigo:int, cuit:str, razonSocial:str):
        super().__init__(codigo, cuit)
        self.razonSocial = razonSocial


class Venta():
    def __init__(self, nro:int, sucursal:int, letra:str , fecha:str, cliente:Cliente ):
        self.nro = nro
        self.sucursal = sucursal
        self.letra = letra
        self.fecha = fecha
        self.cliente = cliente