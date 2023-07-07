def cal_edad():
    if e >= 18:
        print('Eres adulto')
    elif e < 17:
        print('Eres menor de edad')
        return(e)
print("\nPrograma 23.\nPara calcular si es mayor o menor de edad:")
e = float(input("Escribir la edad: "))
(e) = cal_edad()