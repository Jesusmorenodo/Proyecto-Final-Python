def num_par_impar():
    a = 1
    while a <= 16:
        if a % 2 == 1:
            print(a, "es impar")
        else:
            print(a, "es par")
        a += 1 
print("\nPrograma 34.\nImprimir Numeros par y impares:")
num_par_impar()