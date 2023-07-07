def calcular_interes_prestamo(m, tm, pl):
    td = tm / 100
    c = m * (td * (1 + td) ** pl) / ((1 + td) ** pl - 1)
    i = m * td
    cap = c - i
    return (c, i, cap, m)
print("\nPrograma 12.\nCalcula el interés de un préstamo:")
m = float(input("Ingrese el monto del préstamo: "))
tm = float(input("Ingrese la tasa de interés mensual (%): "))
pl = int(input("Ingrese el plazo del préstamo en meses: "))
(c, i, cap, m) = calcular_interes_prestamo(m, tm, pl)
print("La cuota mensual a pagar es:", round(c,2))
print("Del monto total:")
print("Monto para intereses:", round(i,2))
print("Monto para capital:", round(cap,2))