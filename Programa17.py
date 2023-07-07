def convrt_cantidad_unid(g, kg, cm, m):
    g = kg * 1000
    kg = g * 0.001
    cm = m * 100
    m = cm * 0.01
    return (g, kg, cm, m)
print("\nPrograma 17.\nQue convierta cantidades de unidades:")
g= float(input("Ingrese el valor en gramos: "))
kg =float(input("Ingrese el valor en kilogramos: "))
m = float(input("Ingrese el valor en metros: "))
cm = float(input("Ingrese el valor en centímetros:"))
(g, kg, cm, m) = convrt_cantidad_unid(g, kg, cm, m)
print("El resultado es:", g)
print("El resultado es:", kg)
print("El resultado es:", cm)
print("El resultado es:", m)