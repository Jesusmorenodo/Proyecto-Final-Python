def interes_compuesto():
    ti = i / 100
    Cf = Ci * (1 + ti) ** n
    return (Cf)
print("\nPrograma 18.\nQue calcule el interés compuesto:")
Ci = float(input("Ingrese el capital inicial: "))
i = float(input("Ingrese la tasa de interés (%): "))
n = float(input("Ingrese el período del ahorro: "))
(Cf) = interes_compuesto()
print("El capital final es: ", Cf)