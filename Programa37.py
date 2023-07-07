def cal_mayor_de3():
    numeros = []
    contador = 0
    while contador < 3:
        numero = float(input("Escribir número: "))
        numeros.append(numero)
        contador += 1
    mayor = numeros[0]
    i = 1
    while i < 3:
        if numeros[i] > mayor:
            mayor = numeros[i]
        i += 1
    print("El número mayor es:", mayor)
print("\nPrograma 37.\nCalcule el mayor de 3 numeros:")
cal_mayor_de3()