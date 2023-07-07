def Mayor_de_tres(n1, n2, n3):
    mayor = n1
    if n2 > mayor:
        mayor = n2
    if n3 > mayor:
        mayor = n3
    return mayor
print("\nPrograma 24\nPara calcular el mayor de 3 numeros:")
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
mayor = Mayor_de_tres(n1, n2, n3)
print("El mayor número es:",mayor)