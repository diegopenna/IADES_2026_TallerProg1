def mostrarDatosAlumno(nombre, apellido, dni = None, edad = None, domicilio = None,  sexo = None, provincia = None):
    print("ALUMNO:")
    print(f"{apellido}, {nombre}")
    if (dni != None):
        print(f"DNI: {dni}")
    if (edad):
            print(f"Edad: {edad}")
    if (domicilio):
            print(f"Domicilio: {domicilio}")
    if (provincia):
            print(f"Provincia: {provincia}")
    if (sexo):
            print(f"Sexo: {sexo}")


mostrarDatosAlumno("Diego", "Penna", 26620884,None, None, "Masculino")
mostrarDatosAlumno("Maria", "Azucena", sexo="Femenino")
mostrarDatosAlumno(sexo="Masculino", nombre="Javer", apellido="Dominguez")