def compra_articulos():
    CSI = A1 + A2 + A3 + A4 + A5
    CNI = CSI * 1.07
    TDC = CNI
    return (CSI, CNI)
print("\nPrograma 19.\nQue calcule la compra de 5 artículos")
A1 = float(input("Escriba el valor del primer articulo: "))
A2 = float(input("Escriba el valor del segundo articulo: "))
A3 = float(input("Escriba el valor del tercer articulo: "))
A4 = float(input("Escriba el valor del cuarto articulo: "))
A5 = float(input("Escriba el valor del quinto articulo: "))
(CSI, CNI) = compra_articulos()
print("El total de la compra sin impuesto es: ", round(CSI, 2))
print("El total de la compra con impuesto es: ", round(CNI, 2))