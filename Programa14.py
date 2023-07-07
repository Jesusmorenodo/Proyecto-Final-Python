def costo_compra_combustible(Litro):
    a = Litro * 0.98 * 1.07
    return a
print("\nPrograma 14.\nQue calcule el costo de compra de gasolina:")
Litro = float(input("Valor de cantidad de litros: "))
ct = costo_compra_combustible(Litro)
print(ct)