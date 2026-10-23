class Vehiculo:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.anio = 0

    def mostrar(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Anio:", self.anio)


class VehiculoPatentado(Vehiculo):
    def __init__(self):
        super().__init__()
        self.patente = ""
        self.nroMotor = ""
        self.chasis = ""
        self.tipoCombustible = ""

    def mostrar(self):
        super().mostrar()
        print("Patente:", self.patente)
        print("NroMotor:", self.nroMotor)
        print("Chasis:", self.chasis)
        print("Combustible:", self.tipoCombustible)

    


class Automovil(VehiculoPatentado):
    def __init__(self):
        super().__init__()
        self.tipoAuto = "" #'sedan', 'sub'
        self.cantPuertas = 0

    def mostrar(self):
        print("**********************")
        print("Automovil:")
        print("**********************")
        super().mostrar()
        print("Tipo:", self.tipoAuto)
        print("Puertas:", self.cantPuertas)
        print("**********************")

class Camion(VehiculoPatentado):
    def __init__(self):
        super().__init__()
        self.cargaMaxima = 0
        self.tieneAcoplado = False

    def mostrar(self):
        print("**********************")
        print("Camion:")
        print("**********************")
        super().mostrar()
        print("Carga Max.:", self.cargaMaxima)
        print("Acoplado:", self.tieneAcoplado)
        print("**********************")

class Moto(VehiculoPatentado):
    def __init__(self):
        super().__init__()
        self.cilindrada = 0
        self.tipoMoto = ""

    def mostrar(self):
        print("**********************")
        print("Moto:")
        print("**********************")
        super().mostrar()
        print("Cilindrada:", self.cilindrada)
        print("Tipo:", self.tipoMoto)
        print("**********************")


class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__()
        self.rodado = 0
        self.tipoBicicleta = ""

    def mostrar(self):
        print("**********************")
        print("Bicicleta:")
        print("**********************")
        super().mostrar()
        print("Rodado:", self.rodado)
        print("Tipo:", self.tipoBicicleta)
        print("**********************")


unAuto = Automovil()
unAuto.patente = "nvn353"
unAuto.anio = 2023
unAuto.marca = "Ford"

unCamion = Camion()
unCamion.patente = "12344"
unCamion.cargaMaxima = "10 tn"

unaMoto = Moto()
unaMoto.cilindrada = 300

unaBici = Bicicleta()
unaBici.marca = "Shimano"


listaVehiculos =  [unAuto, unCamion, unaMoto, unaBici]

for unVehiculo in listaVehiculos:
    unVehiculo:Vehiculo # no es necesaria esta linea
    unVehiculo.mostrar()




