def cal_nota_final():
    PE1 = N1 * 0.20
    PE2 = N2 * 0.15
    PE3 = N3 * 0.25
    PE4 = N4 * 0.10
    PE5 = N5 * 0.30
    NT = PE1 + PE2 + PE3 + PE4 + PE5 / 100
    return (NT)
print("\nPrograma 16.\nQue calcule la nota final:")
N1 = float(input("Ingresa la primera evaluación: "))
N2 = float(input("Ingresa la segunda evaluación: "))
N3 = float(input("Ingresa la tercera evaluación: "))
N4 = float(input("Ingresa la cuarta evaluación: "))
N5 = float(input("Ingresa la quinta evaluación: "))
(NT) = cal_nota_final()
print("La nota final es de :",round(NT, 2))