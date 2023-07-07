def Cal_temperatura():
    if t < 20:
        if t < 10:
            print("Nivel azul")
        else:
            print("Nivel verde")
    else:
        if t < 30:
            print("Nivel naranja")
        else:
            print("Nivel rojo")
    return (t)
print("\nPrograma 22.\nQue Calcule la temperatura :")
t = float(input("Escriba la temperatura: "))
(t) = Cal_temperatura()