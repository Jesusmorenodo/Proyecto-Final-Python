def calcular_per_rectangulo ():
    P = AB+ BC + CD + DA
    return (P)
print("\nPrograma 5\n Que calcule el perimetro de un rectangulo:")
AB = float(input("Escriba el valor de AB: "))
BC = float(input("Escriba el valor de BC: "))
CD = float(input("Escriba el valor de CD: "))
DA = float(input("Escriba el valor de DA: "))    
P = calcular_per_rectangulo ()
print("El area de un rectangulo es: ", P)