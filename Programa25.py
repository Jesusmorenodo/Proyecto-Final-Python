def cal_descuento():
    Des= PD / 100
    PP = P * Des
    PF = P - PP
    if  PF < 50:
        print("¡Oferta especial!")
        return(PF)
print("\nPrograma 25.\nPara calcular descuentos:")
P = float(input("Ingrese precio original del producto: "))
PD = float(input("Ingrese el porcentaje de descuento: "))
(PF) = cal_descuento()
print("El precio final del producto es:", PF)