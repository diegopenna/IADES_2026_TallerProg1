from inputs import solicitarDecimal, solicitarEntero,solicitarCUIT


cuit = solicitarCUIT()
print(f"Proveedor: {cuit}")

importe = solicitarDecimal("Ingrese un Importe:", 0.01)
iva = solicitarDecimal("Ingrese el porcentaje de iva:", 0.01, 100)
importeIva = importe + importe * iva / 100  
cantidad = solicitarEntero("Ingrese una cantidad:", 0)
print(f"El importe  con iva de {importe} es: {importeIva}") 
print(f"Cantidad: {cantidad}")
print(f"Total: {importeIva * cantidad}") 






