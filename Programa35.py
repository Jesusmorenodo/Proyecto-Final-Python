def Lista_nums():
    for Nums in range(1, 11):
        if Nums > 5:
            print(Nums, "es mayor a 5")
        elif Nums <= 0:
            print(Nums, "es menor a 5")
        else:
            print(Nums, "es menor o igual a 0")
        if Nums == 9:
            break
print("\nPrograma 35.\nLista de numeros del 1 al 10:")
Lista_nums()