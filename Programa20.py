def cal_salario_neto():
    ss = sb * 0.08
    se = sb * 0.02
    i = sb * 0.15
    p = 100
    sn = sb - ss - se - i - p
    return (sn)
print("\nPrograma 20.\nQue calcule el salario neto de un empleado:")
sb = float(input("Ingrese el salario bruto del empleado: "))
(sn) = cal_salario_neto()
print("El salario neto a pagar es:", sn)