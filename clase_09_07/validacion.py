def dividir(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        return resultado
    else:    
        print("No se puede dividir por 0")
        return

num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))
division = dividir(num1, num2)
if division:
    print("La division es:", dividir(num1, num2))