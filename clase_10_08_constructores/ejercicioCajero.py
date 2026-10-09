class CuentaBancaria:
    def __init__(self, numero, titular, saldo = 0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo 

    def __str__(self):
        return f"Cuenta Bancaria {self.numero} ({self.titular} Saldo:{self.saldo})"

    def mostrarDatos(self):
        print(f"Cuenta Bancaria nro {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
        print()

    def depositar(self, importe):
        if importe > 0:
            self.saldo = self.saldo + importe
            return True

        return False
        

#Objeto	Número	Titular	Saldo inicial
#cuenta1	1001	Ana López	$150000
#cuenta2	1002	Carlos Pérez	$80000
#cuenta3	1003	María Gómez	$250000

cuenta1 = CuentaBancaria(1001, "Ana López", 150000.0)
cuenta2 = CuentaBancaria(1002, "Carlos Pérez")
cuenta2.saldo = 80000
cuenta3 = CuentaBancaria(1003,	"María Gómez",	250000.0)

#cuenta1.mostrarDatos()
#cuenta2.mostrarDatos()
#cuenta3.mostrarDatos()

cuenta1.mostrarDatos()
cuenta1.depositar(25000)
cuenta1.mostrarDatos()
cuenta1.depositar(-25000)
cuenta1.mostrarDatos()
