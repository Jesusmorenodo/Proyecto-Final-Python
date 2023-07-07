def calcular_salario_trb():
   SS = S * 0.0514
   SE = S * 0.02
   P = 50
   SN = S - SS - SE - P
   return (SN, SS, SE, P)
print("\nPrograma 13.\nQue calcule salario neto de los trabajadores:")
S = float(input("Ingresa su Salario Mensual: "))
SN, SS, SE, P = calcular_salario_trb()
print("Su saldo a pagar de seguro social es de:", SS)
print("Su saldo a pagar de seguro educativo es de:", SE)
print("Su saldo a pagar de prestamo es de: ", P)
print("El salario a pagar es de:", round(SN, 2))