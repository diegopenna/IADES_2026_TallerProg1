def mostrarMenu(opciones: list, valores : list, titulo:str = None,   pregunta:str = "Elija una opcion:"):
    if titulo != None and titulo != "":
        renglones()
        print(titulo)
        renglones()

    for i in range(len(opciones)):
        print(valores[i], '-' ,  opciones[i])
    while True:
        opc = input(pregunta)
        if opc in valores:
            break
        else:
            print("Opcion incorrecta.")
    return opc

def renglones(cantidad=30, simbolo = "-"): 
    print(simbolo * cantidad)   

opc = mostrarMenu(["Perro", "Gato", "Hamster", "Cobayo"], 
                ["p", "g", "h", "c"],
                "MENU DE MASCOTAS DE LA VETERINARIA 'MI PERRO DINAMITA'",
                "Elija una mascota..."
                )
print(opc)


"""
var1 = "Calculadora"
var2 = ["Suma", "Resta", "Multiplicacion", "Division", "Salida"]
var3 = ["1", "2", "3", "4", "0"]

opc = mostrarMenu(var1, var2, var3)
print(opc)

opc = mostrarMenu("Platos del dia", ["Fideos con tuco", "Ravioles al pesto", "Milanesa Napolitana"], ["a", "b" , "c"], "Elija un plato")
print(opc)
"""



