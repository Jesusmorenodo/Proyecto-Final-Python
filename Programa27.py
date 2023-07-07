def Num_p_n_cero():
    if V == 0:
        print('Es cero')
    elif V < 0:
        print('Es negativo')
    else:
        print('Es positivo')
        return(V)
print("\nPrograma 27.\nQue calcule si el numero es positivo o negativo o 0:")
V= float(input("Escribe el número: "))
(V) = Num_p_n_cero()