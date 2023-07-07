def compra_impuestos():
    PA = A1 + A2 + A3
    I = PA * 1.07
    return (I)
print("\nPrograma 15.\nQue calcule el total de la compra con impuesto:")
A1 = float(input("Escribir valor del articulo 1: "))
A2 = float(input("Escribir valor del articulo 2: "))
A3 = float(input("Escribir valor del articulo 3: "))
(I) = compra_impuestos()
print("total de la compra con el impuesto es de: ", round(I, 2)) 