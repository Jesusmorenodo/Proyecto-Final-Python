def cal_impuestos():
    if s <= 3000:
        i = s * 1.07
        print("Esta persona debe abonar impuestos:", i)
    else:
        print("No debe abonar impuestos")
        return (s)
print("\nPrograma 21.\nCalcular si una persona paga impuestos.")
s = float(input("Escriba el salario: "))
(s) = cal_impuestos()